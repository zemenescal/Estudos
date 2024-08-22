# Estudos - ex105.py
# Autor: José Menescal Neto
# Data: 20/04/22
# Programa para análise de dados informados.

def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7.5:
            r['Situação'] = 'Excelente'
        elif r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


# Programa principal
resp = notas(10, 8, 6, 4, 7, sit=True)
print(resp)
