# Estudos - ex072.py
# Autor: José Menescal Neto
# Data: 24/02/24

##################################################
# # Este programa usa uma tupla para armazenar
# # números por extenso. Quando solicitada uma
# # entrada numérica inteira, entrega o número
# # digitado, por extenso.
##################################################

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número: {cont[num]}')
