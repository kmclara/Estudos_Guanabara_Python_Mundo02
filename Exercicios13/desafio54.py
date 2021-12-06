from datetime import date

contmaior = 0
contmenor = 0

AnoComputador = date.today().year

for Maioridade in range (0,7):
    AnoNascimento = int(input("Digite seu ano de nascimento: "))
    Conta = (AnoComputador-AnoNascimento)
    if Conta <21:
        contmenor+=1
    elif Conta >=21:
        contmaior+=1
print("O total de pessoas maiores de idade é de {}.".format(contmaior))
print("O total de pessoas menores de idade é de {}.".format(contmenor))

print("Obrigada por usar nosso programa!")

      
    