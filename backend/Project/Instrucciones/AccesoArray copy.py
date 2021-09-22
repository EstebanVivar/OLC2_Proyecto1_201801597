from Expresiones.Identificador import Identificador
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
        
       
            
        index = self.valor(self.expresiones[0],tree,table)-1
        value=identificador_result.valor.valor[index]
        print(self.valor(value,tree,table))    
        val2=self.valor2(value,tree,table)
        print("x")
        
        return self.valor2(value,tree,table)
        
    def valor(self,x,tree,table):

        if isinstance(x,Primitivo) and (x.tipo==TipoObjeto.ENTERO or x.tipo==TipoObjeto.BOOLEANO or x.tipo==TipoObjeto.CARACTER or x.tipo==TipoObjeto.DECIMAL or x.tipo==TipoObjeto.CADENA):
            x=x.valor
            if type(x)==str:
                if (x[0]=="'" and x[-0]=="'") or (x[0]=='"' and x[-0]=='"') :
                    return x[1:-1]
            return x
        if isinstance(x,Identificador):
            x=x.ejecutar(tree,table)
            try:
                if x.valor.valor:
                    return(self.valor(x.valor,tree,table))
                else:
                    return x.valor
            except:
                return x.valor

        else:
            return(self.valor(x.valor,tree,table))

    def valor2(self,x,tree,table):

        if isinstance(x,Primitivo) and (x.tipo==TipoObjeto.ENTERO or x.tipo==TipoObjeto.BOOLEANO or x.tipo==TipoObjeto.CARACTER or x.tipo==TipoObjeto.DECIMAL or x.tipo==TipoObjeto.CADENA):
            if type(x.valor)==str:
                if (x.valor[0]=="'" and x.valor[-0]=="'") or (x.valor[0]=='"' and x.valor[-0]=='"'):
                    x.valor= x.valor[1:-1]            
            return x

        elif isinstance(x,Identificador):
            x=x.ejecutar(tree,table)           
            return x

        else:
            return(self.valor2(x.valor,tree,table))

            


    def obtenerNodo(self):
        nodo = NodoReporteArbol("LLAMADA A FUNCION")
        nodo.agregarHijo(str(self.identificador))
        expresioness = NodoReporteArbol("expresionesS")
        for param in self.expresiones:
            expresioness.agregarHijoNodo(param.obtenerNodo())
        nodo.agregarHijoNodo(expresioness)
        return nodo
