# Estudos - ex042.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa que analisa se três segmentos podem formar um triangulo,
# classe do triangulo, seu perímetro e sua área.

l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmento: "))
l3 = float(input("Digite o terceiro segmento: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    p = (l1 + l2 + l3) / 2
    s = (p * (p - l1) * (p - l2) * (p - l3)) ** (1 / 2)
    print('Estes segmentos podem formar um triangulo', end='')
    if l1 == l2 == l3:
        print(f'\033[31m equilátero. Sua área é {s:.2f}m2 e o perímetro {(2 * p):.2f}m')
    elif l1 != l2 != l3 != l1:
        print(f'\033[32m escaleno. Sua área é {s:.2f}m2 e o perímetro {(2 * p):.2f}m')
    else:
        print(f'\033[33m isósceles. Sua área é {s:.2f}m2 e o perímetro {(2 * p):.2f}m')
else:
    print('Os segmentos não podem formar um triângulo')
