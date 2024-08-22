# Estudos - ex096.py
# Autor: José Menescal Neto
# Data: 12/04/22
# Programa que demonstra o uso de função criada para imprimir com formato definido pelo usuário.

def escreva(msg):
    tam = len(msg) + 4
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)


# Programa Principal
escreva('José Menescal Neto')
escreva('Engenheiro')
