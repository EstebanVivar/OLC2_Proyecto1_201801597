from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST


class Identificador(NodoAST):
    def __init__(self, id, fila, columna):
        self.id = id
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        simbolo = table.getTabla(self.id)

        if simbolo == None:
            return Excepcion("Semantico", "Variable " + self.id + " no encontrada.", self.fila, self.columna)
        
        return simbolo.getValor()

    def obtenerNodo(self):
        nodo = NodoReporteArbol("IDENTIFICADOR")
        nodo.agregarHijo(str(self.id))
        return nodo