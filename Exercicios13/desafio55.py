#Contador de pesos

maior = 0
menor = 0

for Pesos in range (1,6):
    PerguntandoOPeso = float(input("Qual o peso da {}ª pessoa: ".format(Pesos)))
    #Se for o peso da primeira pessoa, ela será maior e menor ao mesmo tempo, pois não temos outro valor de comparação:
    if Pesos == 1:
        maior = PerguntandoOPeso
        menor = PerguntandoOPeso
    else:
        if PerguntandoOPeso > maior:
            maior  = PerguntandoOPeso
        if PerguntandoOPeso < menor:
            menor = PerguntandoOPeso
print("O maior peso lido foi de {}Kg!".format(maior))
print("O menor peso lido foi de {}Kg!".format(menor))


