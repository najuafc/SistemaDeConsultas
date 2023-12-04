from pessoa import Paciente, Medico
from consulta import Consulta

def main():

    paciente = Paciente("João", "123456789", "Histórico do paciente")
    medico = Medico("Dra. Maria", "987654321", "Cardiologia")
    consulta = Consulta(paciente=paciente, medico=medico, dataHora=None)

    while True:
        print("\n1 - Marcar consulta")
        print("2 - Alterar consulta")
        print("3 - Verificar consultas")
        print("4 - Cancelar consulta")
        print("5 - Mostrar dados do paciente ou do médico")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            dataHora = input("\nDigite a data e hora da consulta (DD/MM/AAAA - HH:MM): ")
            print(consulta.marcarConsulta(paciente, medico, dataHora))

        elif opcao == "2":

            while True:
                consultas = consulta.mostrarConsultas()

                if consultas:
                    print("\nConsultas disponíveis para alteração:")
                    # Em cada iteração, associa o índice à variável i e o valor à variável consultaDisponivel.
                    for i, consultaDisponivel in enumerate(consultas):
                        print(f"{i+1}- {consultaDisponivel}")

                    numeroConsulta = int(input("\nDigite o número da consulta a ser alterada: "))

                    if 1 <= numeroConsulta <= len(consulta.consultas):
                        novaDataHora = input("Digite a nova data e hora (DD-MM-AAAA HH:MM): ")
                        print(consulta.alterarConsulta(numeroConsulta, novaDataHora))
                        break
                else:
                    print("\nNenhuma consulta disponível para alteração.")
                    break 

        elif opcao == "3":

            consultas = consulta.mostrarConsultas()

            if consultas:
                print("\nConsultas agendadas:")
                for i, consultaDisponivel in enumerate(consultas):
                    print(f"{i+1}- {consultaDisponivel}")
            else:
                print("\nNenhuma consulta agendada.")

        elif opcao == "4":

            consultas = consulta.mostrarConsultas()

            if consultas:
                print("\nConsultas disponíveis para cancelamento:")
                for i, consultaDisponivel in enumerate(consultas):
                    print(f"{i+1}- {consultaDisponivel}")

                numeroConsulta = int(input("\nDigite o número da consulta a ser cancelada: "))

                if 1 <= numeroConsulta <= len(consulta.consultas):
                    print(consulta.cancelarConsulta(consulta.consultas[numeroConsulta - 1]))
                else:
                    print("\nNúmero de consulta inválido. Tente novamente.")

            else:
                print("\nNenhuma consulta disponível para cancelamento.")

        elif opcao == "5":

            while True:
                print("\n1 - Ver dados do paciente")
                print("2 - Ver dados do médico")

                opcaoSubMenu = input('\nEscolha uma opção: ')

                if opcaoSubMenu == "1":
                    infos = paciente.mostrarInformacoes()
                    print(infos)
                    break

                elif opcaoSubMenu == "2":
                    infos = medico.mostrarInformacoes()
                    print(infos)
                    break

                else:
                    print("\nOpção inválida. Tente novamente.")

        elif opcao == "6":
            print('Sistema encerrado.')
            break

        else:
            print("\nOpção inválida. Tente novamente.")

main()