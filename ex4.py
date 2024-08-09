class Lampada:
    def __init__ (self, estado = 0):
        self.estado = estado
    
    def getEstado (self):
        return self.estado
    
    def setEstado (self, estado):
        self.estado = estado
        
    def estaLigada (self):
        if self.estado > 0:
            return True
        else:
            return False