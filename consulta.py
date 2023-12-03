class Consulta:
    def __init__(self, paciente, medico, dataHora):
        self.paciente = paciente
        self.medico = medico
        self.dataHora = dataHora
        
        self.consultas = []

    def marcarConsulta(self, paciente, medico, dataHora):
            novaConsulta = Consulta(self, medico, dataHora)
            self.consultas.append(novaConsulta)
            return f"Consulta do paciente {paciente.nome} marcada para {dataHora} com {medico.nome}."

    def mostrarConsultas(self):
        return [consulta.dataHora for consulta in self.consultas]

    def alterarConsulta(self, consulta, novaDataHora):
        self.dataHora = novaDataHora
        return f"Consulta alterada para {novaDataHora}."

    def cancelarConsulta(self, consulta):
        self.consultas.remove(consulta)
        return f"Consulta cancelada."

  