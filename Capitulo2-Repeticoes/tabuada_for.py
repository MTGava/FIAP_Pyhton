tabuada=int(input("Digite o valor que será multiplicado: "))
print("Tabuada do número", tabuada)
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))