# Estudos - ex039.py
# Autor: José Menescal Neto
# Data: 08/02/22
# Programa para calcular quando deve acontecer o alistamento militar


from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento :"))
idade = atual - nasc
print(f"Quem nasceu em {nasc}, tem {idade} anos em {atual}")
if idade == 18:
    print("Voce deve se alistar \33[4;31mIMEDIATAMENTE!!!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Em {atual}, ainda falta(m) {saldo} ano(s) para seu alistamento")
else:
    atraso = idade - 18
    print(f"Você em {atual}, está atrasado {atraso} ano(s) para seu alistamento.")
