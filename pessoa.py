class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrarInformacoes(self):
        return f'''
Nome: {self.nome}
CPF: {self.cpf}'''

class Paciente(Pessoa):
    def __init__(self, nome, cpf, historicoMedico):
        super().__init__(nome, cpf)
        self.historicoMedico = historicoMedico
    
    def mostrarInformacoes(self):
        infoPaciente = super().mostrarInformacoes()
        return f'''
Dados do paciente:
{infoPaciente}
Histórico médico: {self.historicoMedico}'''

class Medico(Pessoa):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)
        self.especialidade = especialidade

    def mostrarInformacoes(self):
        infoMedico = super().mostrarInformacoes()
        return f'''
Dados do médico:
{infoMedico}
Especialidade: {self.especialidade}'''
