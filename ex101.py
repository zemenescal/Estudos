# Estudos - ex101.py
# Autor: José Menescal Neto
# Data: 19/04/22
# Programa para análise de idade com respeito a votação.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa principal
nasc = int(input('Em que ano você nasceu? : '))
print(voto(nasc))
