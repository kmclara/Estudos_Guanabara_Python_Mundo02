for numeros in range (0,6):
    numeros = int(input("Digite um número: "))
    if numeros%2 == 0:
        print("{} + {} = {}".format(numeros, numeros, numeros+numeros))
    else:
        print("Estes valores não são pares, não podem ser somados!")
        