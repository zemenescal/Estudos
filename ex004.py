# Estudos - ex004.py
# Autor: José Menescal Neto
# Data: 06/02/22

# This program uses a "for" loop to calculate
# the squares and cubes of the first 5 numbers
# 0,1,2,3,4
# Note: Python starts counting at 0 import math


from math import sqrt

for indice in range(1, 11):
    quad = indice ** 2
    cubo = indice ** 3
    raiz_q = sqrt(indice)
    raiz_c = indice ** (1 / 3)
    print(f"Inteiro: {indice:<6} Quadrado: {quad:<6} Cubo: {cubo:<6} Raiz quadrada:"
          f" {raiz_q:<6.3f} Raiz cúbica: {raiz_c:<6.3f}")
# print("A soma entre {} e {} vale {}".format(cube,raiz_q,(cube+raiz_q)))