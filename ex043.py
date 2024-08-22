# Estudos - ex043.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa para calcular o IMC


peso = float(input("Qual é seu peso (kgf): "))
altura = float(input("Qual é sua altura (m): "))
imc = peso / (altura ** 2)
print("Seu IMC é {:.1f}".format(imc))
if imc < 18.4:
    print("Você está \033[31;4mABAIXO DO PESO.")
elif 18.4 <= imc < 25:
    print("Parabens. Você está com o peso \033[034mNORMAL")
elif 25 <= imc < 30:
    print("Você está com \033[33mSOBREPESO")
elif 30 <= imc < 40:
    print("Você está \033[31mOBESO. Cuidado")
elif imc >= 40:
    print("Você está com \033[31;4mOBESIDADE MÓRBIDA!")
