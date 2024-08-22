# Estudos - ex098.py
# Autor: José Menescal Neto
# Data: 16/04/22
# Programa que demonstra o uso de função (definida pelo usuário)
# para contagem regrssiva.


from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('*' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.1)
            cont += p
        print()
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.1)
            cont -= p
        print()
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('*' * 20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
