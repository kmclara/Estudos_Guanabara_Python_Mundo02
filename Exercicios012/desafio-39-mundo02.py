#Desafio 39 - Alistamento Militar 

#Importante o ano do pc: 
from datetime import date 

#Perguntando ao usuário seu ano de nascimento: 
Ano_de_Nascimento = int(input("Qual o ano do seu nascimento? "))

#Fazendo a função do datetime:
Ano_do_Computador = date.today().year

#Cálculo para saber a idade do usuário: 
Idade_do_Usuário = (Ano_do_Computador - Ano_de_Nascimento)

#Delimitando a idade correta: 
Idade_Correta = 18 

#Cálculo para ver se falta ou se passou para realizar o alistamento:
Anos_que_Falta = (Idade_Correta - Idade_do_Usuário)
Anos_que_Passou = (Idade_do_Usuário - Idade_Correta)

#Cálculo mostrando o ano que o usuário deve ou deveria se alistar: 
Deve_se_Alistar = (Ano_do_Computador + Anos_que_Falta)
Deveria_se_Alistar = (Ano_do_Computador - Anos_que_Passou)

#If, elif e else
if Idade_do_Usuário < 18: 
    print("Você ainda não precisa se alistar! Faltam {} anos para você se alistar. Você poderá comparecer no alistamento no ano de {}!".format(Anos_que_Falta, Deve_se_Alistar))
elif Idade_do_Usuário == 18:
    print("De acordo com seu ano de nascimento, você possui {} e já está na hora de fazer o alistamento militar!".format(Idade_do_Usuário))
else: 
    print("Você precisa se alistar! Já se passou {} anos da idade certa para o seu alistamento! Você deveria ter se alistado em: {}!".format(Anos_que_Passou, Deveria_se_Alistar))

print("Obrigada por usar nosso programa! Volte sempre!")