resposta="SIM"

while resposta=="SIM":
    nome=input("Digite o nome: ")
    idade=int(input("Digite o idade: "))

    doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
    while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NAO":
        print("Digite SIM ou NAO")
        doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()

    # PRIMEIRO PROBLEMA A SER RESOLVIDO
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")


    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero=input("Digite o gênero do paciente? FEMININO ou MASCULINO ").upper()
        if genero=="FEMININO" and idade>10:
            gravidez=input("A paciente está grávida? ").upper()
            if gravidez=="SIM":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Pacitente SEM prioridade")

    resposta=input("Digite SIM para continuar: ").upper()