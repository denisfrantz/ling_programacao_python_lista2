class Time:
    def __init__ (self, vitorias, empates, derrotas):
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        self.jogos = vitorias + derrotas + empates
    
    def setVitorias (self, vitorias):
        self.vitorias = vitorias
        self.jogos += vitorias
    
    def setDerrotas(self, derrotas):
        self.derrotas = derrotas
        self.jogos += derrotas
    
    def setEmpates(self, empates):
        self.empates = empates
        self.jogos += empates
        
    def getVitorias(self):
        return self.vitorias
    
    def getEmpates(self):
        return self.empates
    
    def getDerrotas(self):
        return self.derrotas
    
    def getJogos(self):
        return self.jogos