
# Estudos - ex003a.py
# Autor: José Menescal Neto
# Data: 05/02/22
# Programa para converter temperatura (C ->F e F ->C)


print("*" * 26)
print(" Conversor de temperatura")
print("*" * 26)
print()
esc = int(input("Digite: 1 para converter °C -> °F; 2 para converter °F-> °C :"))
if esc == 1:
    temp = float(input("Digite a temperatura em Celsius: "))
    print("A temperatura em Fahrenheit é \033[33m{:.1f}".format((temp * 9) / 5 + 32))
elif esc == 2:
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    print("A temperatura em Celsius é: \033[33m{:.1f}".format((temp - 32) * 5 / 9))
else:
    print()
    print("\033[4;31;40mEscolha não permitida. Digite 1 ou 2\033[m")
