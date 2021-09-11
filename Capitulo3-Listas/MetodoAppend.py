equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()


equipamentoDanificado = input("Qual equipamento foi danificado? ")
for indice in range(0, len(equipamentos)):
    if equipamentoDanificado == equipamentos[indice]:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]
        del departamentos[indice]
        break
    else:
        print("Equipamento inexistente")

for indice in range(0,len(equipamentos)):
    if "Impressora" == equipamentos[indice]:
        valores[indice] = valores[indice] * 0.9
    print("Nome.........: " + equipamentos[indice])
    print("Valor........:", valores[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.: " + departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Serial.:", seriais[indice])
