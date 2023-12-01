from paciente import *

class Teleconsulta:
    def __init__(self, paciente):
        self.paciente = paciente

    def agendarConsulta(self):

        nomePaciente = input('Digite o nome do paciente: ')
        telefonePaciente = input('Digite o telefone do paciente: ')
        modalidadeAtendimento = int(input('''Qual será a modalidade de atendimento? 
                SUS - Digite '1'
                Plano de saúde - Digite '2'
                Particular - Digite '3'
                '''))
        faltaDeAr = int(input('''O paciente possui falta de ar ou dificuldade para respirar?
                            Sim - Digite '1'
                            Não - Digite '2'
                                '''))
        
        if modalidadeAtendimento == 1:
            return 'O paciente será atendido pelo SUS'
        
        elif modalidadeAtendimento == 2:
            planoDeSaude = input('Informe o plano de saúde do paciente: ')
            return f'O paciente será atendido pelo plano de saúde informado: {planoDeSaude}'

        elif modalidadeAtendimento == 3:
            return 'O paciente será atendido pelo particular'

        if faltaDeAr == 1:
            return 'A consulta do paciente é de emergência'
        elif faltaDeAr == 2:
            return 'A consulta do paciente é de rotina'
        
class ConsultaRotina(Teleconsulta):
    def __init__(self, paciente):
        super().__init__(paciente)

class ConsultaEmergencia(Teleconsulta):
    def __init__(self, paciente):
        super().__init__(paciente)


