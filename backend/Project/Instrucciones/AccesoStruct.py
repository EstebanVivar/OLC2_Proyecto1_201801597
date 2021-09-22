from Objeto.Primitivo import Primitivo
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class AccesoStruct(NodoAST):
    def __init__(self, struct, atributo, fila, columna):
        self.struct = struct
        self.atributo = atributo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):        
        struct_result=table.getTabla(self.struct)     
        if struct_result == None:
            return Excepcion("Semantico", "NO SE ENCONTRO EL STRUCT: " + self.struct, self.fila, self.columna)
        contador = 0
        
        for param in struct_result.valor:
            print(param['identificador'])
            print(self.atributo)
            if(param['identificador']==self.atributo):
            # if isinstance(resultExpresion, Excepcion):
            #     return resultExpresion          
                print(param['dato'].getValue())
                return Simbolo(param['identificador'],self.fila,self.columna,param['dato'].getValue()  )
        # nuevaTabla = TablaSimbolos(tree.getTSGlobal())
        
        # # ejecutar EL NODO FUNCION
        # value = result.ejecutar(tree, nuevaTabla)
        # if isinstance(value, Excepcion):
        #     return value
        # return value

    def obtenerNodo(self):
        nodo = NodoReporteArbol("LLAMADA_STRUCT")
        nodo.agregarHijo(str(self.struct))
        atributos = NodoReporteArbol("ATRIBUTO")
        atributos.agregarHijo(self.atributo)
        nodo.agregarHijoNodo(atributos)
        return nodo


