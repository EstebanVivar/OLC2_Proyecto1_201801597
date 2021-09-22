from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST

class Constante(NodoAST):
    def __init__(self, valor, fila, columna):
        self.valor = valor
             # Esta será una instancia de la clase OBJETO
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):  
            if (str(self.valor.getValue()).__contains__("'") or str(self.valor.getValue()).__contains__('"')):
                if((self.valor.getValue()[0]=="'" and self.valor.getValue()[-0]=="'") 
                or (self.valor.getValue()[0]=='"' and self.valor.getValue()[-0]=='"')):  
                    
                    self.valor.setValue(self.valor.getValue()[1:-1])
                    return self.valor
               
            return self.valor

    def obtenerNodo(self):
        nodo = NodoReporteArbol("CONSTANTE")
        nodo.agregarHijo(str(self.valor.valor))
        return nodo
