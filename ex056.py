# Estudos - ex056.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa que calcula média de idades, homem mais velho
# e mulheres abaixo de 20 anos
# from builtins import str, int, range

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulherm20 = 0
for p in range(1, 5):
    print('_____ {}ª Pessoa _____'.format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if p == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        total_mulherm20 += 1
media_idade = soma_idade / 4
print("A média de idade do grupo é {:.1f}".format(media_idade))
print("O homem mais velho tem {} anos e se chama {} ".format(maior_idade_homem, nome_velho))
print("Ao todo são: {} mulher(es) com idade menor que 20 anos".format(total_mulherm20))
