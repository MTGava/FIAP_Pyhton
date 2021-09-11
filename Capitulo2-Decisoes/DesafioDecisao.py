modulo=input("Olá! Você é ADM, USR ou GUEST? ").upper()
if modulo=="ADM" or modulo=="USR":
    genero=input("Beleza " + modulo + "! Qual é o seu gênero? FEM ou MASC: ").upper()
    if modulo=="ADM" and genero=="FEM":
        print("Olá administradora")
    elif modulo=="ADM" and genero=="MASC":
        print("Olá administrador")
    elif modulo=="USR" and genero=="FEM":
        print("Olá usuária")
    elif modulo=="USR" and genero=="MASC":
        print("Olá usuário")
    else:
        print("Digite um gênero válido: FEM ou MASC")
elif modulo=="GUEST":
    print("Olá desconhecido(a)")
else:
    print("Digite se você é ADM, USR ou GUEST")
