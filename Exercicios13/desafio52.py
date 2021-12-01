total = 0 #para saber quantas vezes ele foi divisivel
numeroprimo1 = int(input("Digite um número inteiro: "))
for numeroprimo2 in range (1, numeroprimo1 + 1):
    if numeroprimo1%numeroprimo2 == 0:
        total+=1
print("O número {} foi divisivel {} vezes.".format(numeroprimo1, total))
if total == 2:
    print("Sendo assim, ele é um número primo.")
else:
    print("E por isso ele não é um número primo!")
