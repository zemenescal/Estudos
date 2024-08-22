# Estudos - ex045.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Jogo: Pedra, Papel e Tesoura.


from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura """)
jogador = int(input("Qual é sua jogada? "))
print("\033[33mJO")
sleep(.25)
print("\033[34mKEN")
sleep(.25)
print("\033[35mPO!!!\033[0m")
print()
print("-=" * 14)
print("O Computador escolheu {}".format(itens[computador]))
print("O Jogador escolheu {}".format(itens[jogador]))
print("-=" * 14)
if computador == 0:  # Computador escolheu Pedra
    if jogador == 0:  # Jogador escolheu Pedra
        print("\033[32mEmpate")
    elif jogador == 1:  # Jogador escolheu Papel
        print("\033[34m Jogador ganha")
    elif jogador == 2:  # Jogador escolheu Tesoura
        print("\033[34m Computador ganha")
    else:
        print("\033[31mJogada inválida!")
elif computador == 1:  # Computador escolheu Papel
    if jogador == 0:  # Jogador escolheu Pedra
        print("\033[34m Computador ganha")
    elif jogador == 1:  # Jogador escolheu Papel
        print("\033[32mEmpate")
    elif jogador == 2:  # Jogador escolheu Tesoura
        print("\033[34m Jogador ganha")
    else:
        print("\033[31mJogada inválida!")
elif computador == 2:  # Computador escolheu Tesoura
    if jogador == 0:  # Jogador escolheu Pedra
        print("\033[34m Jogador ganha")
    elif jogador == 1:  # Jogador escolheu Papel
        print("\033[34m Computador ganha")
    elif jogador == 2:  # Jogador escolheu Tesoura
        print("\033[32mEmpate")
    else:
        print("\033[31mJogada inválida!\033[0m")
