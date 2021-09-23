from Instrucciones.Continue import Continue
from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class If(NodoAST):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        condicion = self.condicion.ejecutar(tree, table)
        if condicion.tipo ==TipoObjeto.ERROR: 
            return condicion

        if condicion.tipo == TipoObjeto.BOOLEANO:
            if bool(condicion.valor) == True:   
                nuevaTabla = TablaSimbolos(table,self.fila,self.columna,table.ambito,"IF")     
                for instruccion in self.instruccionesIf:
                    result = instruccion.ejecutar(tree, nuevaTabla)
                    if isinstance(result, Excepcion) :
                        return result
                    if isinstance(result, Continue): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result
            else:            
                if self.instruccionesElse != None:
                    nuevaTabla = TablaSimbolos(table,self.fila,self.columna,table.ambito,"ELSE")     
                    for instruccion in self.instruccionesElse:
                        result = instruccion.ejecutar(tree, nuevaTabla) 
                        if isinstance(result,Excepcion) :
                            return result     
                        
                        if isinstance(result, Continue): return result
                        if isinstance(result, Break): return result
                        if isinstance(result, Return): return result
                elif self.elseIf != None:
                    result = self.elseIf.ejecutar(tree, table)
                    if isinstance(result, Excepcion): 
                        return result
                    if isinstance(result, Continue): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result

        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)


    def obtenerNodo(self):
        nodo = NodoReporteArbol("IF")
        condicionesIf = NodoReporteArbol("CONDICION IF")        
        condicionesIf.agregarHijoNodo(self.condicion.obtenerNodo())
        nodo.agregarHijoNodo(condicionesIf)

        instruccionesIf = NodoReporteArbol("INSTRUCCIONES IF")
        for instr in self.instruccionesIf:
            instruccionesIf.agregarHijoNodo(instr.obtenerNodo())
        nodo.agregarHijoNodo(instruccionesIf)

        if self.instruccionesElse != None:
            instruccionesElse = NodoReporteArbol("INSTRUCCIONES ELSE")
            for instr in self.instruccionesElse:
                instruccionesElse.agregarHijoNodo(instr.obtenerNodo())
            nodo.agregarHijoNodo(instruccionesElse) 
        elif self.elseIf != None:
            nodo.agregarHijoNodo(self.elseIf.obtenerNodo())

        return nodo