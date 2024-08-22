# Módulos - numeros.py
# Autor: José Menescal Neto
# Data: 26/07/24
# Programa que calcula funções
# de um núnero dado.

# importando o módulo uteis.py
from uteis import numeros as nr

# Programa principal entrada dos dados
num = int(input('Digite um valor: '))

# Chama as funções e imprime os resultados
print(f'O fatorial de {num} é {nr.fatorial(num)}')
print(f'O dobro de {num} é {nr.dobro(num)}')
print(f'O triplo de {num} é {nr.triplo(num)}')
