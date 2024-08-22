# Estudos - ex003.py
# Autor: José Menescal Neto
# Data: 04/02/22
# Programa para calcular a área de um triangulo.
"""
nome = input('Nome do aluno ')
print('Prog I é muito legal')
print(123)
altura = 10
print(altura)
print('Vamos pular uma linha \n')
print('O nome do aluno eh', nome)
"""

altura = float(input('Digite a altura do triangulo em m: '))
base = float(input('Digite a base do triangulo em m: '))
area = (base * altura) / 2
print(f"Altura informada -> {altura :.2f}m")
print(f"Base informada -> {base :.2f}m")
print("~" * 36)
print(f"A área do triangulo é: {area :.2f}m²")
