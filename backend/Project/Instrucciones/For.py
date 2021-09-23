from Instrucciones.Continue import Continue
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.NodoAST import NodoAST
from Instrucciones.Return import Return
from Instrucciones.Break import Break
# from Instrucciones.Continue import Continue
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from TablaSimbolos.Simbolo import Simbolo


class For(NodoAST):
    def __init__(self, id, expresion, instrucciones, row, column):
        self.id = id
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.row = row
        self.column = column

    def ejecutar(self, tree, table):
        expresion = self.expresion.ejecutar(tree, table)
        if isinstance(expresion, Excepcion):
            return expresion

        if expresion.tipo != TipoObjeto.CADENA and expresion.tipo != TipoObjeto.RANGO:
            return Excepcion('Semántico', 'Expresion no iterable', self.row, self.column)

        for var in expresion.valor:
            nuevaTabla = TablaSimbolos(table,self.row, self.column,table.ambito)
            simbol = Simbolo(self.id, self.row, self.column,var)
            resul = nuevaTabla.actualizarTabla(simbol)
            for instruccion in self.instrucciones:
                resul = instruccion.ejecutar(tree, nuevaTabla)
                if isinstance(resul, Excepcion):
                    tree.getExcepciones().append(resul)
                    tree.updateConsola(resul)
                if isinstance(resul, Break):
                    return None
                elif isinstance(resul, Continue):
                    break
                elif isinstance(resul, Return):
                    return resul

        return None

    def obtenerNodo(self):
        nodo = NodoReporteArbol("FOR")
        nodo.agregarHijo(str(self.id))
        nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        instrucciones = NodoReporteArbol("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.obtenerNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo
