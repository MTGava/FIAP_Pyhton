from FIAP_NanoCourse.Funcoes.Funcoes_Dicionarios import *

usuarios = {}
opcao = getOpcao()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        setDicionario(usuarios)
    if opcao == 'P':
        login = input("Digite o login que deseja buscar: ").upper()
        getPesquisar(usuarios, login)
    if opcao == 'E':
        login = input("Digite o login que deseja excluir: ").upper()
        objeto = getExcluirLogin(usuarios, login)
    if opcao == 'L':
        getDicionario(usuarios)
    opcao = getOpcao()

print("\n Obrigado por usar a nossa plataforma!")