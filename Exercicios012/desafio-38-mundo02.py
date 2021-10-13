#DESAFIO 38 - QUAL NÚMERO É MAIOR, MENOR OU IGUAL? 

#Pedindo ao usuário dois valores numericos: 
número_usuário_um = int(input("Digite o primeiro valor: "))
número_usuário_dois = int(input("Digite o segundo valor: "))


#Verificando quem é maior:
if número_usuário_dois>número_usuário_um: 
    print("O número {} é maior que o número {}!".format(número_usuário_dois, número_usuário_um))
elif número_usuário_um<número_usuário_dois:
    print("O número {} é menor que o número {}!".format(número_usuário_um, número_usuário_dois))
elif número_usuário_um>número_usuário_dois: 
    print("O número {} é maior que o número {}!".format(número_usuário_um, número_usuário_dois))
elif número_usuário_dois<número_usuário_um: 
    print("O número {} é menor que o número {}!".format(número_usuário_dois, número_usuário_um))
elif número_usuário_um == número_usuário_dois: 
    print("Ambos os números {} e {} são valores iguais!".format(número_usuário_um, número_usuário_dois))

print("Obrigada por usar nosso programa! Volte sempre!")