# Estudos - ex064.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa que recebe diversos números, informa quantos foram, sua soma e média.

# from builtins import int

cont = soma = 0
num = float(input("Digite um número ou [99999] para parar: "))
while num != 99999:
    soma += num
    cont += 1
    num = float(input("Digite um número ou [99999] para parar: "))
print(f"Você digitou {cont} número(s), resultando em uma soma de: {soma:.2f} e média de: {(soma / cont):.2f}")
