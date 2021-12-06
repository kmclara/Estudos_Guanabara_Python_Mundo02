SomaIdade = 0 
MediaIdade = 0
IdadeHomemVelho = 0
NomeHomemVelho = ''

for Questions in range (1,5):
    NomeUsuario = input("Nome da {}ª pessoa: ".format(Questions))
    IdadeUsuario = int(input("Idade da {}ª pessoa: ".format(Questions)))
    SexoUsuario = input("Sexo da {}ª pessoa: ".format(Questions))
    SomaIdade += IdadeUsuario
    if Questions == 1 and SexoUsuario in "Mm":
        IdadeHomemVelho = IdadeUsuario
        NomeHomemVelho = NomeUsuario
    if SexoUsuario in "Mm" and IdadeUsuario > IdadeHomemVelho:
        IdadeHomemVelho = IdadeUsuario
        NomeHomemVelho = NomeUsuario
MediaIdade = SomaIdade/4
print("A média da idade do grupo é de {} anos!".format(MediaIdade))
print("O homem mais velho tem {} anos e se chama {}!".format(IdadeHomemVelho, NomeHomemVelho))
