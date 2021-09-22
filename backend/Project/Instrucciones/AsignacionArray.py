from Expresiones.Constante import Constante
from Instrucciones.AccesoArray import Acceso_Array
from Expresiones.Aritmetica import Aritmetica
from typing import Any
from Expresiones.Identificador import Identificador
from Expresiones.Array import Array
from Objeto.Primitivo import Primitivo
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion

from Abstract.Objeto import TipoObjeto
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class AsignacionArray(NodoAST):
    def __init__(self, identificador, expresiones,expresion, fila, columna):
        self.identificador = identificador
        self.expresiones = expresiones
        self.expresion=expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):        
        identificador_result=table.getTabla(self.identificador)     
        if identificador_result == None:
            return Excepcion("Semantico", "NO SE ENCONTRO EL identificador: " + self.identificador, self.fila, self.columna)
        contador = 0
        resultado=False
        for expresion in self.expresiones:  
            if not resultado:  
                if isinstance( expresion,Identificador):
                    expresion=expresion.ejecutar(tree,table)                         
                    resultado=identificador_result.valor.valor[expresion.valor-1]
                elif isinstance( expresion,Acceso_Array):
                    expresion=expresion.ejecutar(tree,table)  
                    resultado=identificador_result.valor.valor[expresion.valor.valor-1]                    
                else:
                    resultado=identificador_result.valor.valor[expresion.valor.valor-1] 
            else:
                if isinstance( expresion,Identificador):
                    expresion=expresion.ejecutar(tree,table)
                    
                    try:
                        resultado=resultado.valor.expresiones[expresion.valor-1]
                    except:
                        try:
                            resultado=resultado.expresiones[expresion.valor-1]
                        except:
                            print("x")
               
                elif isinstance( expresion,Acceso_Array):
                    expresion=expresion.ejecutar(tree,table)
                    
                    try:
                        resultado=resultado.valor.expresiones[expresion.valor.valor-1]
                    except:
                        try:
                            resultado=resultado.expresiones[expresion.valor.valor-1]
                        except:
                            print("x")
                else: 
                    try:
                        resultado=resultado.valor.expresiones[expresion.valor.valor-1]
                    except:
                        try:
                            resultado=resultado.expresiones[expresion.valor.valor-1]
                        except:
                            print("x")
        if isinstance( self.expresion,Aritmetica):
                self.expresion=self.expresion.ejecutar(tree,table)
        if isinstance( self.expresion,Constante):
                self.expresion=self.expresion.valor
        if isinstance(resultado.valor,Constante):
            resultado=resultado.valor                           
        resultado.valor=self.expresion
       
            

    def obtenerNodo(self):
        nodo = NodoReporteArbol("ACCESO_ARRAY")
        nodo.agregarHijo(str(self.identificador))
        expresioness = NodoReporteArbol("expresionesS")
        for param in self.expresiones:
            expresioness.agregarHijoNodo(param.obtenerNodo())
        nodo.agregarHijoNodo(expresioness)
        return nodo
