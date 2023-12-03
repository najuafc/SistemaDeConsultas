from pessoa import Paciente, Medico

def main():
    paciente = Paciente("João", "123456789", "Histórico do Paciente")
    medico = Medico("Dra. Maria", "987654321", "Cardiologia")

    while True:
        print("\n1 - Marcar Consulta")
        print("2 - Alterar Consulta")
        print("3 - Verificar Consultas")
        print("4 - Cancelar Consulta")
        print("5 - Mostrar dados do paciente ou do médico")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            dataHora = input("Digite a data e hora da consulta (DD/MM/AAAA - HH:MM): ")
            print(paciente.marcarConsulta(medico, dataHora))

        elif opcao == "2":

            while True:
                consultas = paciente.mostrarConsultas()

                if consultas:
                    print("Consultas disponíveis para alteração:")
                    for i, consulta in enumerate(consultas):
                        print(f"{i+1}- {consulta}")
                    numeroConsulta = int(input("Digite o número da consulta a ser alterada: "))
                    if 1 <= numeroConsulta <= len(paciente.consultas):
                        novaDataHora = input("Digite a nova data e hora (YYYY-MM-DD HH:MM): ")
                        print(paciente.alterarConsulta(paciente.consultas[numeroConsulta - 1], novaDataHora))
                        break
                    
                    else:
                        print("Número de consulta inválido. Tente novamente.")
                else:
                    print("Nenhuma consulta disponível para alteração.")
                    break 

        elif opcao == "3":

            consultas = paciente.mostrarConsultas()

            if consultas:
                print("Consultas agendadas:")
                for i, consulta in enumerate(consultas):
                    print(f"{i+1}- {consulta}")
            else:
                print("Nenhuma consulta agendada.")

        elif opcao == "4":

            consultas = paciente.mostrarConsultas()

            if consultas:
                print("Consultas disponíveis para cancelamento:")
                for i, consulta in enumerate(consultas):
                    print(f"{i+1}- {consulta}")

                numeroConsulta = int(input("Digite o número da consulta a ser cancelada: "))

                if 1 <= numeroConsulta <= len(paciente.consultas):
                    print(paciente.cancelarConsulta(paciente.consultas[numeroConsulta - 1]))
                else:
                    print("Número de consulta inválido. Tente novamente.")

            else:
                print("Nenhuma consulta disponível para cancelamento.")

        elif opcao == "5":

            while True:
                print("1 - Ver dados do paciente")
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
                    print("Opção inválida. Tente novamente.")

        elif opcao == "6":
            break

        else:
            print("Opção inválida. Tente novamente.")

main()