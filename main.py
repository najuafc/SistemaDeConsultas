from pessoa import Paciente, Medico
from consulta import Consulta, Modalidade

def main():
    paciente = Paciente("João", 25, "123456789", "Histórico do Paciente")
    medico = Medico("Dra. Maria", 35, "987654321", "Cardiologia")

    while True:
        print("\n1. Marcar Consulta")
        print("2. Alterar Consulta")
        print("3. Verificar Consultas")
        print("4. Cancelar Consulta")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            dataHora = input("Digite a data e hora da consulta (DD/MM/AAAA - HH:MM): ")
            paciente.marcarConsulta(medico, dataHora)
            print("Consulta marcada!")

        # DANDO ERRO NA FUNÇAO ALTERAR
        elif opcao == "2":
            consultas = paciente.mostrarConsultas()
            if consultas:
                print("Consultas disponíveis para alteração:")
                for i, consulta in enumerate(consultas):
                    print(f"{i+1}- {consulta}")
                numeroConsulta = int(input("Digite o número da consulta a ser alterada: "))
                novaDataHora = input("Digite a nova data e hora (YYYY-MM-DD HH:MM): ")
                paciente.alterarConsulta(paciente.consultas[numeroConsulta+1], novaDataHora)
                print("Consulta alterada!")
            else:
                print("Nenhuma consulta disponível para alteração.")

        elif opcao == "3":
            consultas = paciente.mostrarConsultas()
            if consultas:
                print("Consultas agendadas:")
                for i, consulta in enumerate(consultas):
                    print(f"{i+1}- {consulta}")
            else:
                print("Nenhuma consulta agendada.")

        elif opcao == "4":
            if paciente.mostrarConsultas():
                numeroConsulta = int(input("Digite o número da consulta a ser cancelada: "))
                paciente.cancelarConsulta(paciente.consultas[numeroConsulta+1])
                print("Consulta cancelada!")
            else:
                print("Nenhuma consulta disponível para cancelamento.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

main()