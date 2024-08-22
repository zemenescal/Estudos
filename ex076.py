# Estudos - ex076.py
# Autor: José Menescal Neto
# Data: 24/02/24

##################################################
# # Este programa usa uma tupla para armazenar
# # string e números. Retorna uma listagem de
# # artigos e seus preços em forma tabular.
##################################################

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)
print('-' * 43)
print(f'{'Listagem de preços de mat. escolares':^43}')
print('-' * 43)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f' {listagem[pos]:.<32}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 43)