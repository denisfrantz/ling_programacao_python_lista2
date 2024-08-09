class Lampada:
    def __init__ (self, marca, cor, watt, preco):
        self.marca = marca
        self.cor = cor
        self.watt = watt
        self.preco = preco
    
    def setMarca (self, marca):
        self.marca = marca
        
    def setCor (self, cor):
        self.cor = cor
        
    def setWatt (self, watt):
        self.watt = watt
        
    def setPreco (self, preco):
        self.preco = preco
        
    def getMarca (self):
        return self.marca
    
    def getCor (self):
        return self.cor
    
    def getWatt (self):
        return self.watt
    
    def getPreco (self):
        return self.preco