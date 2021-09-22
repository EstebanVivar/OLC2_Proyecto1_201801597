from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Simbolo import Simbolo
from Objeto.StructPrimitivo import StructPrimitivo
from Instrucciones.Funcion import Funcion
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Llamada(NodoAST):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        result = tree.getFuncion(self.nombre)  
        if result == None:  
            struct_result=tree.getStruct(self.nombre)        
            if struct_result == None:
                return Excepcion("Semantico", "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)
            contador = 0
            for expresion in self.parametros:  
                resultExpresion = expresion.ejecutar(tree, table)
                # if isinstance(resultExpresion, Excepcion):
                #     return resultExpresion

                if struct_result.parametros[contador].get('tipo',False):
                    
                #Falta para los que no tienen tipo
                    if (resultExpresion.tipo==struct_result.parametros[contador]['tipo']):
                        struct_result.parametros[contador]['dato']=resultExpresion                 
                    else:
                        struct_result.parametros[contador]['dato']=resultExpresion 
                contador += 1
            return StructPrimitivo(self.nombre,struct_result.parametros)            
        nuevaTabla = TablaSimbolos(table,result.fila,result.columna,table.ambito,self.nombre,"FUNCION")
        if len(result.parametros) != len(self.parametros):
            return Excepcion("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
        contador = 0
        for expresion in self.parametros: 
            resultExpresion = expresion.ejecutar(tree, table)
            if isinstance(resultExpresion, Excepcion):
                return resultExpresion
            if result.parametros[contador].get('tipo',False):
                if (resultExpresion.tipo==result.parametros[contador]['tipo']):
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion):
                        return resultTabla
            else:
                simbolo = Simbolo(str(result.parametros[contador]['identificador']), self.fila, self.columna, resultExpresion)
                resultTabla = nuevaTabla.setTabla(simbolo)
                
                if isinstance(resultTabla, Excepcion):
                    return resultTabla
            contador += 1
        value = result.ejecutar(tree, nuevaTabla)
        table.addTabla(self.nombre,nuevaTabla)
        if isinstance(value, Excepcion):
            return value
        return value

    def obtenerNodo(self):
        nodo = NodoReporteArbol("LLAMADA A FUNCION")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoReporteArbol("PARAMETROS")
        for param in self.parametros:
            parametros.agregarHijoNodo(param.obtenerNodo())
        nodo.agregarHijoNodo(parametros)
        return nodo
