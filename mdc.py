#  Cálculo do mdc entre dois números
#  Data:12/10/2022

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


# main

print('     Cálculo do mdc de dois números')
print('*' * 40)
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
mdc = mdc(n1, n2)
print(mdc)
