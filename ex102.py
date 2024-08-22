# Estudos - ex102.py
# Autor: José Menescal Neto
# Data: 20/04/22
# Programa para calcular fatorial usando função.

def fatorial(n, show=False):
    '''-> Calcula o fatorial de um número
    :parâmetro n: Número usado no cálculo de seu fatorial;
    :parâmetro show: (opcional) Explicita ou não os cálculos;
    :return: Entrega o fatorial do número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(' x ', end="")
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5, show=True))
# help(fatorial)
