# Estudos - ex085.py
# Programa que seleciona em uma digitação de
# 7 números, os pares e os impares.


num = [[], []]
valor = 0
for c in range(1, 8):  # Serão digtados 7 números
    valor = int(input(f"Digite o {c}º número: "))
    if valor % 2 == 0:  # Se o número for par
        num[0].append(valor)  # Coloca o no. par na 1a. lista
    else:
        num[1].append(valor)  # Coloca o no. impar na 2a. lista
print("~" * 55)
num[0].sort()
num[1].sort()
print(f"Os números pares digitados foram: {num[0]}")
print(f"Os números ímpares digitados foram:{num[1]}")
