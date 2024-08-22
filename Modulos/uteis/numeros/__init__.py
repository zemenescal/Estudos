# Módulo uteis.py
# 26/07/2024

# função fatorial
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


# função dobro
def dobro(n):
    return n * 2


# função triplo
def triplo(n):
    return n * 3