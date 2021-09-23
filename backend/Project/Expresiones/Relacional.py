from Instrucciones.AccesoArray import Acceso_Array
from Instrucciones.AccesoStruct import AccesoStruct
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Constante import Constante
from Expresiones.Identificador import Identificador
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, OperadorRelacional

class Relacional(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna

    
    def ejecutar(self, tree, table):
        res_left = self.OperacionIzq.ejecutar(tree, table)
        res_right = self.OperacionDer.ejecutar(tree, table)
        try:
            if isinstance (res_right.valor.valor,Constante):
                res_right=res_right.valor.valor
        except:
            pass
        
        if isinstance(res_left,Aritmetica):
            res_left=res_left.ejecutar(tree, table)
        if isinstance(res_right,Aritmetica):
            res_right=res_right.ejecutar(tree, table)

        if isinstance(res_left,Identificador):
            res_left=res_left.ejecutar(tree, table)
        if isinstance(res_right,Identificador):
            res_right=res_right.ejecutar(tree, table)
       
        if isinstance(res_left,Acceso_Array):
            res_left=res_left.ejecutar(tree, table)
        if isinstance(res_right,Acceso_Array):
            res_right=res_right.ejecutar(tree, table)
        
        
        if isinstance(res_left,Constante):
            res_left=res_left.valor
        if isinstance(res_right,Constante):
            res_right=res_right.valor

        try:
            if(res_left.tipo == TipoObjeto.ERROR):
                return res_left   
        except:
            if isinstance(res_left,Identificador):
                res_left=res_left.ejecutar(tree, table)
        
            print("x")
        if isinstance(res_left,Acceso_Array):
                res_left=res_left.ejecutar(tree, table)  
        
        if isinstance(res_right,Acceso_Array):
                res_right=res_right.ejecutar(tree, table) 
        if(res_right.tipo == TipoObjeto.ERROR):
            return res_right;  
        
        if (self.operador==OperadorRelacional.MAYORIGUAL):
            return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() >= res_right.getValue());
        

        if (self.operador==OperadorRelacional.MAYOR):            
            try:
                return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() > res_right.getValue());
            except:
                if isinstance(res_left,Acceso_Array):
                    res_left=res_left.ejecutar(tree, table) 
                if isinstance(res_left,Acceso_Array):
                    res_left=res_left.ejecutar(tree, table) 
                return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() > res_right.getValue());
            
                print("X")
                
        if (self.operador==OperadorRelacional.MENORIGUAL):
            return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() <= res_right.getValue());
        
        if (self.operador==OperadorRelacional.MENOR):
            return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() < res_right.getValue());
        
        if (self.operador==OperadorRelacional.COMPARACION):
            return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() == res_right.getValue());
        
        if (self.operador==OperadorRelacional.DIFERENTE):
            return Primitivo(TipoObjeto.BOOLEANO, res_left.getValue() != res_right.getValue());
        


        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.operador}",self.fila,self.columna);
   
    

    def obtenerNodo(self):
        nodo = NodoReporteArbol("RELACIONAL")
        nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
        nodo.agregarHijo(str(self.operador.name))
        nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        
        
        return nodo
        