from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.TablaSimbolos import TablaSimbolos


class Return(NodoAST):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        result = self.expresion.ejecutar(tree, table)
        if isinstance(result, Excepcion):
            return result
        self.result = result  
        return self

    def obtenerNodo(self):
        nodo = NodoReporteArbol("RETURN")

        nodo.agregarHijoNodo(self.expresion.obtenerNodo())

        return nodo
