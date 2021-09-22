from Instrucciones.Asignacion import Asignacion
from TablaSimbolos.Simbolo import Simbolo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Funcion(NodoAST):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        nuevaTabla = TablaSimbolos(table,self.fila,self.columna,"FUNCION",self.nombre,"FUNCION") 
        for instruccion in self.instrucciones:    
            value = instruccion.ejecutar(tree,nuevaTabla)
            if isinstance(value, Excepcion):
                tree.getExcepciones().append(value)
                tree.updateConsola(value)
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsola(err.toString())
            if isinstance(value, Return): 
                return value.result
            
            
           
        # table.addTabla(self.nombre,nuevaTabla)     
        return value

    def obtenerNodo(self):
        nodo = NodoReporteArbol("FUNCION")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoReporteArbol("PARAMETROS")
        for param in self.parametros:
            parametro = NodoReporteArbol("PARAMETRO")
            try:
                parametro.agregarHijo(param["tipo"])
            except:
                pass
            parametro.agregarHijo(param["identificador"])
            parametros.agregarHijoNodo(parametro)
        nodo.agregarHijoNodo(parametros)

        instrucciones = NodoReporteArbol("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.obtenerNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo