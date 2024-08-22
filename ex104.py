# Estudos - ex104.py
# Autor: José Menescal Neto
# Data: 20/04/22
# Programa para validação de dados na entrada

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
