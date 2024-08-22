# Estudos - ex009.py
# Autor: José Menescal Neto
# Data: 09/02/22
# Programa para gera tabuada de somar ou multiplicar


print(f"  Programa para gerar tabuada ")
print("-~-" * 8)
num = int(input("Digite um número: "))
resp = str(input("O que desejas? Soma ou Multiplicação [Soma(s)/Multiplicação(m)]:"))
if resp in "Ss":
    print("Soma")
    for c in range(1, 11):
        print(f" {num: >2} + {c: >2} = {num + c: >3}")
else:
    print("Multiplicação")
    for c in range(1, 11):
        print(f" {num: >2} X {c: >2} = {num * c: >3}")
print("-~" * 8)
print("Como solicitado.")
