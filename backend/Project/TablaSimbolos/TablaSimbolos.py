

from Abstract.Objeto import TipoObjeto
from TablaSimbolos.Excepcion import Excepcion



class TablaSimbolos:
    def __init__(self,anterior = None,fila=0,columna=0,ambito="GLOBAL",id="",tipo="ENTORNO" ):
        self.tabla = {}
        self.anterior = anterior
        self.ambito=ambito
        self.tipo=tipo
        self.id =id
        self.fila=fila
        self.columna=columna

        self.tipo=tipo

    def setTabla(self, simbolo):     
        if simbolo.id in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id] = simbolo
            return None

    def addTabla(self,id, tabla):
            self.tabla[id] = tabla

    
    
    def getTabla(self, id):            
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id] 
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla :
                tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                
                return None             
            else:
                tablaActual = tablaActual.anterior
        
        self.tabla[simbolo.id] = simbolo
        return None 
        
    def actualizar(self, simbolo):        
        self.tabla[simbolo.id] = simbolo
        return None 
    
    
