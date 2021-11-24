for c in range (1,6):
    print("Oi")
print("FIM")

#Usando iterador para indicar o que irá acontecer:
#Quero que ele conta de 6 até 0, ou seja, de trás pra frente
for n in range (6,0,-1):
    print(n)
print("Fim")
#Quero que ele conte de 0 á 7 de dois em dois:
for m in range (0,7,2):
    print(m)
print("Fim")
#Quero que ele conte de 1000 á 0 de 2 em 2:
for j in range (1000,0,-2):
    print(j)
print("FIM")
#Quero que ele conte de 0 a 100 de 3 em 3:
for y in range (0,100,3):
    print(y)
print("FIM")

o = int(input("Digite um número: "))
for p in range (0, o+1):
    print(p)
print("Fim")

g = int(input("Inicio: "))
l = int(input("Fim: "))
s = int(input("Passo: "))

for ç in range (g, l, s):
    print(ç)