SomaIdade = 0 
MediaIdade = 0
IdadeHomemVelho = 0
NomeHomemVelho = ''
ContMulher20 = 0

for Questions in range (1,5):
    NomeUsuario = input("Nome da {}ª pessoa: ".format(Questions)).strip()
    IdadeUsuario = int(input("Idade da {}ª pessoa: ".format(Questions)))
    SexoUsuario = input("Sexo da {}ª pessoa [M/F]: ".format(Questions)).strip()
    SomaIdade += IdadeUsuario
    if Questions == 1 and SexoUsuario in "Mm":
        IdadeHomemVelho = IdadeUsuario
        NomeHomemVelho = NomeUsuario
    if SexoUsuario in "Mm" and IdadeUsuario > IdadeHomemVelho:
        IdadeHomemVelho = IdadeUsuario
        NomeHomemVelho = NomeUsuario
    if SexoUsuario in "Ff" and IdadeUsuario < 20:
        ContMulher20 += 1
MediaIdade = SomaIdade/4
print("A média da idade do grupo é de {} anos!".format(MediaIdade))
print("O homem mais velho tem {} anos e se chama {}!".format(IdadeHomemVelho, NomeHomemVelho))
print("Ao todo são {} mulheres com menos de 20 anos!".format(ContMulher20))
