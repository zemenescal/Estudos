# Estudos - ex100.py
# Autor: José Menescal Neto
# Data: 16/04/22
# Programa que cria uma função para sorteio
# aleatório e apresenta a soma dos números pares.

from time import sleep
from random import randint

def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 9)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(.1)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando-se os valores pares de {lista}, temos: {soma}')

# Programa principal
num = list()
sorteia(num)
somaPar(num)
print('*' * 20)
print('  Como solicitado.')
print('*' * 20)
