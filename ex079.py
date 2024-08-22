# Estudos - ex079.py
# Autor: José Menescal Neto
# Data: 24/02/24

##################################################
# # Este programa usa uma lista vazia para armazenar
# # números digitados sem duplicação. Retorna uma
# # lista com os valores em ordem crescente.
##################################################

numeros = list()
while True:
    n = int(input('Digite um valor inteiro: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Número existente. Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 20)
numeros.sort()
print(f'Você digitou os números {numeros}')
