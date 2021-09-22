from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, OperadorAritmetico


class Array(NodoAST):
    def __init__(self,  expresiones, fila, columna):
        
        self.expresiones = expresiones
        self.fila = fila
        self.columna = columna

    

    def ejecutar(self, tree, table):
                
        lista=list()   
        
        for i in self.expresiones:
            lista.append(Primitivo(TipoObjeto.ARREGLO,i))

        return Primitivo(TipoObjeto.ARREGLO,lista);              
    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("ARREGLO")
       
        # nodo.agregarHijo(str(self.expresiones))
        if (type(self.expresiones)==list):
            for exp in self.expresiones:
                nodo.agregarHijoNodo(exp.obtenerNodo())
        
        return nodo