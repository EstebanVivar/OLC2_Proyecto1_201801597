
from Instrucciones.For import For
from Expresiones.Constante import Constante
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, OperadorAritmetico


class Aritmetica(NodoAST):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
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
        if self.OperacionIzq!=None:
            res_left = self.OperacionIzq.ejecutar(tree, table)
            
            try:
                if res_left.tipo==TipoObjeto.RANGO:
                    res_left=res_left.valor.valor.valor
                if(res_left.tipo == TipoObjeto.ERROR):
                    return res_left;  
            except:
                print("X")
        
        if self.OperacionDer!=None:
            res_right = self.OperacionDer.ejecutar(tree,table)
            try:
                if isinstance(res_right,Constante):
                    res_right=res_right.valor
                if(res_right.tipo == TipoObjeto.ERROR):
                    return res_right;  
            except:
                print("asda") 

        if (self.operador==OperadorAritmetico.MAS):
            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, int(str(res_left.getValue())) + int(str(res_right.getValue())));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(str(res_left.getValue())) + float(str(res_right.getValue())));

            
        
        elif (self.operador==OperadorAritmetico.MENOS):
            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, int(str(res_left.getValue())) - int(str(res_right.getValue())));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(str(res_left.getValue())) - float(str(res_right.getValue())));

        
        elif (self.operador==OperadorAritmetico.POR): 
            
            if(res_left.tipo==TipoObjeto.RANGO) and type(res_right.valor)==int:
                 res_left.tipo=TipoObjeto.ENTERO
            elif(res_left.tipo==TipoObjeto.RANGO) and type(res_right.valor)==float:
                 res_left.tipo=TipoObjeto.DECIMAL
            elif(res_left.tipo==TipoObjeto.RANGO) and type(res_right.valor)==str:
                 res_left.tipo=TipoObjeto.CADENA
            
            if(res_right.tipo==TipoObjeto.RANGO) and type(res_right.valor)==int:
                res_right.tipo=TipoObjeto.ENTERO
            elif(res_right.tipo==TipoObjeto.RANGO) and type(res_right.valor)==float:
                res_right.tipo=TipoObjeto.DECIMAL
            elif(res_right.tipo==TipoObjeto.RANGO) and type(res_right.valor)==str:
                res_right.tipo=TipoObjeto.CADENA
        

            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, int(str(res_left.getValue())) * int(str(res_right.getValue())));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(str(res_left.getValue())) * float(str(res_right.getValue())));

            if(res_left.tipo==TipoObjeto.CADENA and res_right.tipo==TipoObjeto.CADENA) :
                return Primitivo(TipoObjeto.CADENA, str(res_left.getValue()) + str(res_right.getValue()));
        
        elif (self.operador==OperadorAritmetico.DIV):
            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.DECIMAL, float(int(res_left.getValue()) / int(res_right.getValue())));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(str(res_left.getValue())) / float(str(res_right.getValue())));


        elif (self.operador==OperadorAritmetico.POT):  
            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, int(int(str(res_left.getValue())) ** int(str(res_right.getValue()))));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(float(str(res_left.getValue())) ** float(str(res_right.getValue()))));

            if(res_left.tipo==TipoObjeto.CADENA and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.CADENA, str(self.x(str(res_left.getValue()) ,int(str(res_right.getValue())))));

        elif (self.operador==OperadorAritmetico.MOD):  
            if(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, int(int(str(res_left.getValue())) % int(str(res_right.getValue()))));            

            elif(res_left.tipo==TipoObjeto.ENTERO and res_right.tipo==TipoObjeto.DECIMAL
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.ENTERO
            or res_left.tipo==TipoObjeto.DECIMAL and res_right.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(float(str(res_left.getValue())) % float(str(res_right.getValue()))));
        
        elif (self.operador==OperadorAritmetico.NEG):  
            if(res_left.tipo==TipoObjeto.ENTERO):
                return Primitivo(TipoObjeto.ENTERO, -int(res_left.getValue()));            
            elif(res_left.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, -float(res_left.getValue()));          

        elif (self.operador==OperadorAritmetico.COMA):  
            return Primitivo(TipoObjeto.CADENA, str(res_left.getValue()) + str(res_right.getValue()));  

        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.operador}",self.fila,self.columna);

    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("ARITMETICA")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.obtenerNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionIzq.obtenerNodo())
        
        return nodo