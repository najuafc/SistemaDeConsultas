from consulta import Consulta, Modalidade

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, historicoMedico):
        super().__init__(nome, idade, cpf)
        self.historicoMedico = historicoMedico
        self.consultas = []

    def marcarConsulta(self, medico, dataHora):
        nova_consulta = Consulta(self, medico, dataHora)
        self.consultas.append(nova_consulta)
        return f"Consulta marcada para {dataHora} com {medico.nome}."

    def mostrarConsultas(self):
        return [consulta.dataHora for consulta in self.consultas]

    def alterarConsulta(self, consulta, novaDataHora):
        consulta.alterarData(novaDataHora)
        return f"Consulta alterada para {novaDataHora}."

    def cancelarConsulta(self, consulta):
        self.consultas.remove(consulta)
        return f"Consulta cancelada para {consulta.dataHora}."

class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, especialidade):
        super().__init__(nome, idade, cpf)
        self.especialidade = especialidade

    def mostrarInformacoes(self):
        infoMedico = super().mostrarInformacoes()
        return f"{infoMedico}, Especialidade: {self.especialidade}"