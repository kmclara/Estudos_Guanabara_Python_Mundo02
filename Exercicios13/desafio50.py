soma = 0
for numeros in range (0,6):
    numeros = int(input("Digite um número: "))
    if numeros%2 == 0:
        soma = soma + numeros
print("A soma dos numeros que você colocou foi de {}!".format(soma))
