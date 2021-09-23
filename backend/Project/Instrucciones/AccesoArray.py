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


class Acceso_Array(NodoAST):
    def __init__(self, identificador, expresiones, fila, columna):
        self.identificador = identificador
        self.expresiones = expresiones
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
                    try:    
                        if expresion.tipo==TipoObjeto.RANGO:
                            resultado=identificador_result.valor.valor[expresion.valor.valor.valor.valor-1]                     
                        
                        else:
                            resultado=identificador_result.valor.valor[expresion.valor-1]
                    except:
                        resultado=identificador_result.valor.valor[expresion.valor-1]
                    
                        print("aver")
                elif isinstance( expresion,Acceso_Array):
                    expresion=expresion.ejecutar(tree,table)  
                    resultado=identificador_result.valor.valor[expresion.valor.valor-1]                    
                elif isinstance( expresion,Aritmetica):
                    expresion=expresion.ejecutar(tree,table)  
                    try:
                        resultado=identificador_result.valor.valor[expresion.valor.valor-1]
                    except:
                        resultado=identificador_result.valor.valor[expresion.valor-1]
                    
                else:
                    try:
                        resultado=identificador_result.valor.valor[expresion.valor.valor-1].valor
                    except:
                        try:
                            resultado=identificador_result.valor.valor[expresion.valor.valor-1]
                        except:
                            print("XD")
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
                elif isinstance( expresion,Aritmetica):
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
                        resultado=resultado.valor.valor[expresion.valor.valor-1]
                    except:
                        try:
                            resultado=resultado.valor.expresiones[expresion.valor.valor-1]
                        except:
                            try:
                                resultado=resultado.expresiones[expresion.valor.valor-1]
                            except:
                                print("x")
        try:
            return resultado.valor
        except:
            if isinstance( resultado,Aritmetica):
                resultado=resultado.ejecutar(tree,table)
                return resultado
            if isinstance( resultado,Array):
                return resultado.expresiones

    def obtenerNodo(self):
        nodo = NodoReporteArbol("ACCESO_ARRAY")
        nodo.agregarHijo(str(self.identificador))
        expresioness = NodoReporteArbol("expresionesS")
        for param in self.expresiones:
            expresioness.agregarHijoNodo(param.obtenerNodo())
        nodo.agregarHijoNodo(expresioness)
        return nodo
