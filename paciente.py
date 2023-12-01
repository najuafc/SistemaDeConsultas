class Paciente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class PacienteSUS(Paciente):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)

class PacientePlanoDeSaude(Paciente):
    def __init__(self, nome, telefone, planoDeSaude):
        super().__init__(nome, telefone)
        self.planoDeSaude = planoDeSaude
    
    def informarPlanoDeSaude(self):
        self.planoDeSaude = input('Informe o plano de saúde do paciente: ')

class PacienteParticular(Paciente):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)

    def informarMetodoPagamento(self):
        valor = input('''Selecione o método de pagamento:
                      Cartão de crédito - Digite '1'
                      Cartão de débito - Digite '2'
                      PIX - Digite '3'
                      ''')