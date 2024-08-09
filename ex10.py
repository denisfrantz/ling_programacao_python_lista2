class Livro:
    def __init__ (self, nome, autor, numPaginas):
        self.nome = nome
        self.autor = autor
        self.numPaginas = numPaginas
    
    def setNome (self, nome):
        self.nome = nome
    
    def setAutor (self, autor):
        self.autor = autor
    
    def setNumPaginas (self, numPaginas):
        self.numPaginas = numPaginas

    def getNome (self):
        return self.nome
    
    def getAutor (self):
        return self.autor
    
    def getNumPaginas (self):
        return self.numPaginas