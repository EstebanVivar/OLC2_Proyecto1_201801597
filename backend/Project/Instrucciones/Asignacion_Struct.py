from Abstract.Objeto import TipoObjeto
from Abstract.NodoReporteArbol import NodoReporteArbol
from TablaSimbolos.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST
from TablaSimbolos.Simbolo import Simbolo


class Asignacion_Struct(NodoAST):
    def __init__(self,struct,atributo,expresion, fila, columna):
        self.struct = struct
        self.atributo = atributo
        self.expresion = expresion        
        self.fila = fila
        self.columna = columna

    def ejecutar(self, tree, table):
        struct = table.getTabla(self.struct)
        if struct==None:            
            return Excepcion("Semantico", "Struct no existente", self.fila, self.columna)
        
        for i in range(len(struct.valor)):
            if struct.valor[i]['identificador']==self.atributo:   
                parametro=struct.valor[i]
                value = self.expresion.ejecutar(tree, table)
                parametro['dato']=value
        if value!=None:
            d_type= self.expresion.ejecutar(tree, table).tipo
        simbolo = False

        if  self.expresion.ejecutar(tree, table).tipo==TipoObjeto.ERROR:
            return value;        
        
        else:
            if d_type==None:
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)
            elif d_type=="Int64" and type(value.getValue())==int:            
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)
            elif d_type=="Float64" and type(value.getValue())==float:            
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)
            elif d_type=="Char" and type(value.getValue())==str and value.getValue()[0]=="'"and value.getValue()[-0]=="'":   
                value.valor = value.getValue()[1:-1]
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)
            elif d_type=="String" and type(value.getValue())==str:      
                value.valor = value.getValue()[1:-1]      
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)        
            elif d_type=="Bool" and type(value.getValue())==bool:         
                simbolo = Simbolo(self.struct, self.fila, self.columna, value)
            
                
            if simbolo:
                result = table.actualizarTabla(simbolo)     # Si no se encuentra el simbolo, lo agrega 

                if isinstance(result,Excepcion): 
                    return result
                else:
                    return None

    def obtenerNodo(self):
        nodo = NodoReporteArbol("ASIGNACION")
        nodo.agregarHijo(str(self.struct))
        nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        return nodo