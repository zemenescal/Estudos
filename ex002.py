# Estudos - ex002.py
# Autor: José Menescal Neto
# Data: 04/02/22

##################################################
# # Este programa usa o laço "for" para calcular
# # o quadrado e o cubo dos n primeiros números.
# # 0,1,2,3,4, posições para n=5.
# # Nota: Python inicia o contador na posição "0".
##################################################

n = int(input("Digite um número: "))
for indice in range(1, n + 1):
    quadrado = indice ** 2
    cubo = indice ** 3
    raiz_q = indice ** (1 / 2)
    raiz_c = indice ** (1 / 3)
    print(
        f'  Número -> {indice:>4}   Quadrado -> {quadrado:>6}   Cubo -> {cubo:>8}   '
        f'Raiz quadrada -> {raiz_q:>6.4f}   Raiz cubica -> {raiz_c:>6.4f}')
print("~" * 110)
print(f"Missão cumprida para o(s) {n} primeiro(s) número(s)")