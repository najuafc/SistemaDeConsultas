class Consulta:
    def __init__(self, paciente, medico, dataHora):
        self.paciente = paciente
        self.medico = medico
        self.dataHora = dataHora
        
        self.consultas = []

    def marcarConsulta(self, paciente, medico, dataHora):
        novaConsulta = Consulta(paciente, medico, dataHora)
        self.consultas.append(novaConsulta)
        return f"Consulta do paciente {paciente.nome} marcada para {dataHora} com {medico.nome}."

    def mostrarConsultas(self):
        # Cria uma lista que retorna a dataHora de cada uma das consultas na lista self.consultas
        return [consulta.dataHora for consulta in self.consultas]
    
    def alterarConsulta(self, numeroConsulta, novaDataHora):
        if 1 <= numeroConsulta <= len(self.consultas):
            consultaAlterada = self.consultas[numeroConsulta - 1]  # Obtém a consulta específica da lista de consultas
            consultaAlterada.dataHora = novaDataHora
            return f"Consulta alterada para {novaDataHora}."
        else:
            return "Número de consulta inválido. Tente novamente."

    def cancelarConsulta(self, consulta):
        self.consultas.remove(consulta)
        return f"Consulta cancelada."

  