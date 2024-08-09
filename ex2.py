class LampadaTresEstados:
    def __init__ (self, estado = "apagado"):
        self.estado = estado
        if (estado == "meiaLuz"):
            self.estado = "meiaLuz"
        elif (estado == "acessa"):
            self.estado = "acessa"
    
    def setEstado (self, estado):
        self.estado = estado
        
    def getEstado (self):
        return self.estado