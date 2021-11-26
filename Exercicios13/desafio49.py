NumeroDaTabuada = int(input("Digite um número para que façamos a tabuada dele: "))

soma = 0
for Tabuada in range (0, 11):
    print("{} x {} = {}".format(NumeroDaTabuada, Tabuada, NumeroDaTabuada*Tabuada))
    soma += Tabuada
