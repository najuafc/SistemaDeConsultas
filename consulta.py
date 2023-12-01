class Consulta:
    def __init__(self, paciente, medico, dataHora):
        self.paciente = paciente
        self.medico = medico
        self.dataHora = dataHora

    def realizarConsulta(self):
        return f"Consulta realizada em {self.dataHora}"

    def alterarData(self, novadataHora):
        self.dataHora = novadataHora
        return f"Data da consulta alterada para {self.dataHora}."

    def cancelarConsulta(self):
        return f"Consulta cancelada."

class Modalidade(Consulta):
     def __init__(self, paciente, medico, dataHora, modalidade):
        super().__init__(paciente, medico, dataHora)
        self.modalidade = modalidade
  