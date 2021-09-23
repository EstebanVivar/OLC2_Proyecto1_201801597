from Expresiones.Aritmetica import Aritmetica
from Expresiones.Array import Array
from re import A
from Expresiones.Identificador import Identificador
from Objeto.Primitivo import Primitivo
from Expresiones.Constante import Constante
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO


class Imprimir(NodoAST):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        for expre in self.expresion:
            value = expre.ejecutar(tree, table)

            if isinstance(value, Excepcion):
                return value
            if isinstance(value,Constante):
                value=value.valor
            try:
                if value.tipo==TipoObjeto.ARREGLO:
                    tree.updateConsola("[")
                    cont = 0
                    for val in value.valor:
                        print (isinstance(val.valor,Aritmetica))
                        if isinstance(val.valor,Aritmetica):
                            val=val.valor.ejecutar(tree,table)
                            tree.updateConsola(val.valor)
                            tree.updateConsola(",")
                            continue
                        
                        try:
                            tree.updateConsola(val.valor.valor.valor)
                        except:
                            if isinstance(val.valor,Array):
                                self.valueGet(tree,val.valor)
                        cont += 1
                        if cont < len(value.valor):
                            tree.updateConsola(",")

                    tree.updateConsola("]")
                else:
                    if value != None:
                        if type(value) == str:
                            if value.valor == True or value.valor == False:
                                tree.updateConsola(str(value.valor).lower())
                        else:
                            try:
                                tree.updateConsola(value.valor) 
                            except:print("x")   
            except:
                if value != None:
                    if type(value) == str:
                        if value.valor == True or value.valor == False:
                            tree.updateConsola(str(value.valor).lower())
                    else:
                        try:
                            tree.updateConsola(value.valor) 
                        except:print("x")         
        return value

    def valueGet(self,tree,array):
        for exp in array.expresiones:
            tree.updateConsola(exp.valor.valor) 

    def obtenerNodo(self):
        nodo = NodoReporteArbol("IMPRIMIR")
        if (type(self.expresion)==list):
            for exp in self.expresion:
                nodo.agregarHijoNodo(exp.obtenerNodo())

        else:
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        return nodo
