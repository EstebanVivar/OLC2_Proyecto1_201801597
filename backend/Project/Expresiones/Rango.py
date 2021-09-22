from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, OperadorAritmetico


class Rango(NodoAST):
    def __init__(self,  OperacionIzq, OperacionDer, fila, columna):
        
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna

    def x(self,cadena,repeat):
        string =""
        for i in range(repeat):
            string+=cadena
        return string

    def ejecutar(self, tree, table):
                
        lista=list()    
        
        res_left = self.OperacionIzq.ejecutar(tree,table)
        if self.OperacionDer==None:     
                for i in res_left.getValue():
                    lista.append(Primitivo(TipoObjeto.RANGO,i))
                
                return Primitivo(TipoObjeto.RANGO,lista);           
                
        res_right = self.OperacionDer.ejecutar(tree,table)
        if(res_left.tipo == TipoObjeto.ERROR):
            return res_left;   
        if(res_right.tipo == TipoObjeto.ERROR):
            return res_right;        
        
        for i in range(res_left.getValue(), res_right.getValue()+1):
            lista.append(Primitivo(TipoObjeto.ENTERO,i))

        return Primitivo(TipoObjeto.RANGO,lista);              
    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("RANGO")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
            nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        else:
            nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
        
        return nodo