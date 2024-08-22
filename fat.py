# Estudos - fat.py
# Autor: José Menescal Neto
# Data: 26/07/24
# Programa que calcula o fatorial
# de um núnero dado.

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
