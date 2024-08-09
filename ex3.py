class LampadaTresEstados:
    def __init__ (self, estado = 0):
        self.estado = estado
        
    def setEstado (self, estado):
        self.estado = estado
    
        if estado == 100:
            self.estado = "acesa"
            
        elif estado == 0:
            self. estado = "apagada"
            
    def getEstado (self):
        return self.estado