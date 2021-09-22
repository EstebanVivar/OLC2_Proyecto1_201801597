from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST

class Continue(NodoAST):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        return self

    def obtenerNodo(self):
        nodo = NodoReporteArbol("CONTINUE")
        return nodo