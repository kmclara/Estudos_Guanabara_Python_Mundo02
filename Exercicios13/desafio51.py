PrimeiroTermo = int(input("Digite o primeiro termo: "))
Razão = int(input("Digite a razão: "))

TermoDescoberto = PrimeiroTermo + (10-1) * Razão
TermoDescoberto += 1 

for Progressao in range (PrimeiroTermo, TermoDescoberto, Razão):
    print(Progressao)

#InicioProgressao = int(input("Digite um numero que irá iniciar sua progressão: "))
#Razão = int(input("Digite de quanto em quanto ela deve ocorrer: "))

#for ProgressaoA in range (InicioProgressao, 11, Razão):
 #   print(ProgressaoA)