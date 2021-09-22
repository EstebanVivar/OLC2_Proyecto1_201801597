from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import OperadorLogico

class Logica(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
    
    def ejecutar(self, tree, table):
        if self.OperacionIzq != None:
            res_left = self.OperacionIzq.ejecutar(tree, table)
            if(res_left.tipo == TipoObjeto.ERROR):
                return res_left;
        res_right = self.OperacionDer.ejecutar(tree, table)
        if(res_right.tipo == TipoObjeto.ERROR):
            return res_right;
        
        
        
        if (self.operador==OperadorLogico.OR):
            return Primitivo(TipoObjeto.BOOLEANO, bool(res_left.getValue()) or bool(res_right.getValue()));
        elif (self.operador==OperadorLogico.NOT):
            return Primitivo(TipoObjeto.BOOLEANO, not bool(res_right.getValue()));
        elif (self.operador==OperadorLogico.AND):
            return Primitivo(TipoObjeto.BOOLEANO, bool(res_left.getValue()) and bool(res_right.getValue()));
        
        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.operador}",self.fila,self.columna);

            
        

    def obtenerNodo(self):
        nodo = NodoReporteArbol("LOGICA")
        if self.OperacionIzq != None:
            nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        
        return nodo