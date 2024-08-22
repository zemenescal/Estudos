# Estudos - ex063.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Série de Fibonacci e razão entre o último e
# o penúltimo termo.

'''
print("~" * 40)
print("|          Série de Fibonacci          |")
print("~" * 40)
n = int(input("Quantos termos você deseja mostrar?: "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont cont + 1
print("-> Fim")

'''


print("~" * 40)
print("|          Série de Fibonacci          |")
print("~" * 40)
n = int(input("Quantos termos você deseja mostrar?: "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2} -> são os dois primeiros")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3: >6}", end="")
    t1 = t2
    t2 = t3
    cont += 1
print()
print(f"   Razão {t2 / t1:.5f}   ")
print("-> Fim")
