#DESAFIO 36 - EMPRESTIMO BANCARIO 

#Conduta da "empresa"
print("Apenas se seu salário não exceder 30% da prestação do aluguel, seu emprestimo dará APROVADO. Caso contrário, NEGADO!")

#Perguntando ao usuário o salario dele, o valor da casa e em quantos anos ele irá pagar:
salario_usuário = float(input("Qual o valor do seu salário? "))
valor_da_casa = float(input("Qual o valor da casa? "))
quantos_anos_aluguel = float(input("Quantos anos pretende pagar o aluguel? "))

#Cálculo do valor da prestação mensal: 
cálculo_prestação_mensal =  valor_da_casa / (quantos_anos_aluguel*12)

#Cálculo caso exceder 30% o valor do salario: 
exceder_do_salario = (salario_usuário*0.30) 

#Se, senão se, senão: 
if cálculo_prestação_mensal > exceder_do_salario: 
    print("O aluguel que você irá pagar é de R${:.2f}.".format(cálculo_prestação_mensal))
    print("Porém o valor excedeu 30%, sendo assim, seu emprestimo foi negado!")
else: 
    print("O aluguel que você irá pagar é de R${:.2f}.".format(cálculo_prestação_mensal))
    print("O valor NÃO excedeu 30%, emprestimo APROVADO!")

print("Obrigada por usar nosso programa! Volte sempre!")