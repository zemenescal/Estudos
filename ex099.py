# Estudos - ex099.py
# Autor: José Menescal Neto
# Data: 16/04/22
# Programa que exemplifica a criação de função sem argumentos definidos.


from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados ...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valor(es) ao todo.')
    print(f'O maior valor é {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
