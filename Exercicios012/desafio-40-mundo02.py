#DESAFIO 40 - MÉDIA DE NOTAS

#Perguntando ao aluno duas notas para calcular a média dele: 
Nota_1 = float(input("Adicione a primeira nota: "))
Nota_2 = float(input("Adicione a primeira nota: "))

#Cálculando a média: 
Cálculo_da_Média = (Nota_1 + Nota_2)/2

#If, elif e else: 
if Cálculo_da_Média < 5.0: 
    print("De acordo com sua média {}, você foi REPROVADO sua média foi menor que 5.0! \nEstude mais na próxima!".format(Cálculo_da_Média))
elif Cálculo_da_Média>=5.0 and Cálculo_da_Média<=6.9:
    print("De acordo com suas notas {} e {}, você está de RECUPERAÇÃO! Sua média foi de {}. \nSe atente mais aos estudos!".format())