class Ponto2D:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.posicao = (x, y)
        
    def setX (self, x):
        self.x = x
    
    def setY (self, y):
        self.y = y
    
    def getX (self):
        return self.x
    
    def getY (self):
        return self.y
    
    def getPosicao (self):
        return self.posicao