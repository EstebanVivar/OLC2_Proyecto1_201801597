from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class While(NodoAST):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        while True:
            condicion = self.condicion.ejecutar(tree, table)
            if isinstance(condicion, Excepcion): return condicion

            if condicion.tipo == TipoObjeto.BOOLEANO:
                if bool(condicion.valor) == True: 
                    nuevaTabla = TablaSimbolos(table,self.fila,self.columna,table.ambito)     
                    for instruccion in self.instrucciones:
                        result = instruccion.ejecutar(tree, nuevaTabla) 
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)

    def obtenerNodo(self):
        nodo = NodoReporteArbol("WHILE")

        instrucciones = NodoReporteArbol("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.obtenerNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo