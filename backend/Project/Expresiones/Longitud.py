from Instrucciones.AccesoArray import Acceso_Array
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import OperadorLogico

class Longitud(NodoAST):
    def __init__(self, array,  fila, columna):
        self.array = array
        self.fila = fila
        self.columna = columna
        self.lenght = 0
    
    def ejecutar(self, tree, table):
        resultado=self.array.ejecutar(tree,table)
        if isinstance(self.array,Acceso_Array):
            resultado=self.array.ejecutar(tree,table)
            return Primitivo(TipoObjeto.ENTERO,len(resultado));
        self.lenght=len(resultado.valor)
        
        return Primitivo(TipoObjeto.ENTERO,len(resultado.valor)); 

            
        

    def obtenerNodo(self):
        nodo = NodoReporteArbol("LONGITUD")
        
        nodo.agregarHijo(str(self.lenght))
        # nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        
        return nodo