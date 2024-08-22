# Estudos - ex086.py
# Autor: José Menescal Neto
# Data: 3/04/22
# Programa que recebe diversos, informa quantos foram, sua soma e média.
# Programa para montar Matriz


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para {(l + 1)},{(c + 1)}: "))
print("~" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
