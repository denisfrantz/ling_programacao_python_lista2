class Musica:
    def __init__ (self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def setNome (self, nome):
        self.nome = nome
    
    def setArtista (self, artista):
        self.artista = artista
    
    def setDuracao (self, duracao):
        self.duracao = duracao
    
    def getNome (self):
        return self.nome
    
    def getArtistas (self):
        return self.artista
    
    def getDuracao (self):
        return self.duracao