# Estudos - ex064a.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa loop infinito até que digite um controle.


s = cont = 0
while True:
    n = float(input("Digite o número e [99999] para parar: "))
    if n == 99999:
        break
    cont += 1
    s += n
print(f"Você digitou {cont} número(s), resultando em uma soma de: {s:.1f} e média de: {(s / cont):.2f}")
