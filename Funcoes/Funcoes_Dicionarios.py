def getOpcao():
    opcao = input("O que deseja realizar?" +
                  "\n<I> - Para Inserir um usuário" +
                  "\n<P> - Para Pesquisar um usuário" +
                  "\n<E> - Para Excluir um usuário" +
                  "\n<L> - Para Listar um usuário: ").upper()
    return opcao


def setDicionario(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]


def getPesquisar(dicionario, login):
    lista = dicionario.get(login)
    if lista != None:
        print("\nNome...........: " + lista[0])
        print("último acesso..: " + lista[1])
        print("Última estação.: " + lista[2] + "\n")


def getExcluirLogin(dicionario, login):
    if dicionario.get(login) != None:
        del dicionario[login]
        print("\nUsuário: ", login, " excluído\n")
        return
    print("\n Usuário: ", login," inexistente\n")


def getDicionario(dicionario):
    for chave, valor in dicionario.items():
        print("\nObjeto.....")
        print("Login: ", chave)
        print("Dados: ", valor, "\n")
