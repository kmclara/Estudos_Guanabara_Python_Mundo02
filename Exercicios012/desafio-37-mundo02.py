#DESAFIO 37 - CONVERSOR DE BASES NÚMERICAS

#Pedindo ao usuário um número inteiro para a conversão: 
número_inteiro = int(input("Digite um número inteiro: "))

#Pedindo ao usuário que escolha uma das 3 bases para realizar a conversão: 
print("""Escolha uma das bases para que se realize a conversão: 
[1] BINÁRIO
[2] OCTAL 
[3] HEXADECIMAL """)

Opção_do_usuário = int(input("Sua opção: "))

#If, Elif or Else
if Opção_do_usuário == 1: 
    print("{} convertido para BINÁRIO é igual á {}!".format(número_inteiro,bin(número_inteiro) [2: ] ))
elif Opção_do_usuário == 2:
    print("{} convertido para OCTAL é igual á {}.".format(número_inteiro, oct(número_inteiro) [2: ]))
elif Opção_do_usuário == 3:
    print("{} convertido para HEXADECIMAL é igual á {}.".format(número_inteiro, hex(número_inteiro) [2: ]))
else: 
    print("Opção invalida! Tente novamente!")

print("Obrigada por usar nosso programa! Volte sempre")