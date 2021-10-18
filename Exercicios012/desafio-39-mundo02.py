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
if idade < 18: 
    print("Você ainda não precisa se alistar! Falta {} anos para você se alistar. Você poderá comparecer no alistamento no ano de {}!".format(Idade_Falta, Deve_se_Alistar))