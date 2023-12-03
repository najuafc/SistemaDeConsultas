from consulta import Consulta, Modalidade

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
        self.consultas = []

    def marcarConsulta(self, medico, dataHora):
        novaConsulta = Consulta(self, medico, dataHora)
        self.consultas.append(novaConsulta)
        return f"Consulta do paciente {self.nome} marcada para {dataHora} com {medico.nome}."

    def mostrarConsultas(self):
        return [consulta.dataHora for consulta in self.consultas]

    def alterarConsulta(self, consulta, novaDataHora):
        consulta.alterarData(novaDataHora)
        return f"Consulta alterada para {novaDataHora}."

    def cancelarConsulta(self, consulta):
        self.consultas.remove(consulta)
        return f"Consulta cancelada."
    
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
