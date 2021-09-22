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
            if value.tipo==TipoObjeto.ARREGLO:
                tree.updateConsola("[")
                cont = 0
                for val in value.valor:

                    
                    tree.updateConsola(val.valor.valor.valor)
                    cont += 1
                    if cont < len(value.valor):
                         tree.updateConsola(",")

                tree.updateConsola("]")
            elif value != None:
                if type(value) == str:
                    if value.valor == True or value.valor == False:
                        tree.updateConsola(str(value.valor).lower())
                else:
                    try:
                        tree.updateConsola(value.valor) 
                    except:print("x")         
        return value

    def valor(self,x,tree, table):
        if isinstance(x,Identificador):
            valor=x.ejecutar(tree, table)
            return valor.valor;

        if isinstance(x,Constante):
            x = x.valor
            self.valor(x,tree,table)
        if isinstance(x,Primitivo):
            return x.valor        
        else:
            self.valor(x,tree,table)

    def obtenerNodo(self):
        nodo = NodoReporteArbol("IMPRIMIR")
        if (type(self.expresion)==list):
            for exp in self.expresion:
                nodo.agregarHijoNodo(exp.obtenerNodo())

        else:
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        return nodo
