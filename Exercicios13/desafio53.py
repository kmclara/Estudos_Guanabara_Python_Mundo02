Frase = str(input("Digite uma frase: ")).strip().upper()
SeparandoPalavras = Frase.split()
JuntandoPalavras = ''.join(SeparandoPalavras)
for frase in JuntandoPalavras:
    if frase == " ".join(reversed(JuntandoPalavras)):
        print("É um Polidromo")
    else:
        print("Não é um Polidromo")
        break
    


