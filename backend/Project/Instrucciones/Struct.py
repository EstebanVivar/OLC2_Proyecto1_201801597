from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Tipo import TIPO
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Struct(NodoAST):
    def __init__(self, nombre, parametros, mutable, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.mutable=mutable
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        return None

    def obtenerNodo(self):
        nodo = NodoReporteArbol("STRUCT")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoReporteArbol("PARAMETROS")
        for param in self.parametros:
            parametro = NodoReporteArbol("PARAMETRO")
            parametro.agregarHijo(param["identificador"])
            parametros.agregarHijoNodo(parametro)
        nodo.agregarHijoNodo(parametros)    
        return nodo