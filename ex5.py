class Professor:
    def __init__ (self, nome, disciplina, codigo):
        self.nome = nome
        self.disciplina = disciplina
        self.codigo = codigo
    
    def setNome (self, nome):
        self.nome = nome
    
    def setDisciplina (self, disciplina):
        self.disciplina = disciplina
    
    def setCodigo (self, codigo):
        self.codigo = codigo
    
    def getNome (self):
        return self.nome
    
    def getDisciplina (self):
        return self.disciplina
    
    def getCodigo (self):
        return self.codigo