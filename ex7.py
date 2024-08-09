class Empregado:
    def __init__ (self, nome, departamento, horasTrabalhadasNoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasNoMes = horasTrabalhadasNoMes
        self.salarioPorHora = salarioPorHora
        self.salarioMensal = self.salarioPorHora * self.horasTrabalhadasNoMes
    
    def getNome (self):
        return self.nome
    
    def getDepartamento (self):
        return self.departamento
    
    def getHorasTrabalhadasNoMes (self):
        return self.horasTrabalhadasNoMes
    
    def getSalarioPorHora (self):
        return self.salarioPorHora
    
    def mostraDados (self):
        return "Nome: ", self.nome, "\nDepartamento: ", self.departamento, "\nSalário mensal: " + str(self.salarioMensal) + "\nSalário por hora: " + str(self.salarioPorHora) + "\nHoras trabalhadas no mês: " + str(self.horasTrabalhadasNoMes)
    
    def calculaSalarioMensal (self):
        self.salarioMensal = self.salarioPorHora * self.horasTrabalhadasNoMes
        return self.salarioMensal
