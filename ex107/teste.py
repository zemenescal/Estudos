from ex107 import moeda

p = float(input(f'Digite o a moeda: R$'))
print(f'A metade de R${p:.2f} é: R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é: R${moeda.dobro(p):.2f}')
print(f'Aumentando em 10%, fica: R${moeda.aumentar(p,10):.2f}')
print(f'Diminuindo 5% de R${p:.2f}, fica: R${moeda.diminuir(p,5):.2f}')