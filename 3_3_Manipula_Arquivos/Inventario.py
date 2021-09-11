from FIAP_NanoCourse.Funcoes.Funcoes_Arquivos import *

inventario = {}

opcao = chamarMenu()

while 0 < opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
        #for linha in resultado:
        #    separacao = linha[linha.find(";") + 1:-1]
        #    data = separacao[0:separacao.find(";")]
        #    separacao = separacao[separacao.find(";") + 1:-1]
        #    descricao = separacao[0:separacao.find(";")]
        #    departamento = linha[linha.rfind(";") + 1:-1] #right find direita p/ esquerda
        #    print("Data.........: ", data)
        #    print("Descrição....: ", descricao)
        #    print("Departamento.: ", departamento)
    opcao = chamarMenu()
