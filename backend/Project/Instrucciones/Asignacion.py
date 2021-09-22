from Expresiones.Aritmetica import Aritmetica
from Expresiones.Constante import Constante
from Instrucciones.Struct import Struct
from Abstract.Objeto import Objeto, TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Simbolo import Simbolo


class Asignacion(NodoAST):
    def __init__(self, identificador, expresion,tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        value = self.expresion.ejecutar(tree, table)
        if self.tipo!=None:
            d_type= self.tipo
        simbolo = False
        if isinstance(value,Constante):
            value=value.valor
        if isinstance(value,Aritmetica):
            value=value.ejecutar(tree, table)
        if value==None:
            return value
        if value.tipo==TipoObjeto.RANGO:
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value.valor)
        elif value.tipo==TipoObjeto.STRUCT:
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value.valor)
        elif value.tipo==TipoObjeto.ERROR:
            return value;  
        elif self.tipo==None:
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)
        elif d_type==TipoObjeto.ENTERO and type(value.getValue())==int:            
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)
        elif d_type==TipoObjeto.DECIMAL and type(value.getValue())==float:            
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)
        elif d_type==TipoObjeto.CARACTER and type(value.getValue())==str and value.getValue()[0]=="'"and value.getValue()[-0]=="'":   
            value.valor = value.getValue()[1:-1]
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)
        elif d_type==TipoObjeto.CADENA and type(value.getValue())==str:      
            value.valor = value.getValue()[1:-1]      
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)        
        elif d_type==TipoObjeto.BOOLEANO and type(value.getValue())==bool:         
            simbolo = Simbolo(self.identificador, self.fila, self.columna, value)
        
            
        if simbolo:
            result = table.actualizarTabla(simbolo)   
            
            if isinstance(result,Excepcion): 
                return result
            else:
                return None

    def obtenerNodo(self):
        nodo = NodoReporteArbol("ASIGNACION")
        nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        return nodo