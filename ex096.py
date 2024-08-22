# Estudos - ex096.py
# Autor: José Menescal Neto
# Data: 12/04/22
# Programa que demonstra o uso de função (definida pelo usuário).


def area(larg, comp):
    s = l * c
    print()
    print(f'A área do terreno com largura  de {l:.2f}m e comprimento {c:.2f}m é {s:.2f}m²')


# Programa Principal
print('     Planimetria')
print('-' * 30)
l = float(input('Qual a largura em (m): '))
c = float(input('Qual o comprimento em (m):'))
area(l, c)
