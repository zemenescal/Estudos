# Estudos - ex044.py
# Autor: José Menescal Neto
# Data: 31/03/22
# Programa que calcula as prestações de crediário


print("{: ^46}".format(" Lojas O Baratão "))
valor = float(input("Total de compras (R$) "))
print("""     Formas de pagamento
[ 1 ] - à vista com dinheiro ou cheque;
[ 2 ] - à vista com cartão;
[ 3 ] - 2x com cartão;
[ 4 ] - 3x ou mais com cartão.""")
print()
op = int(input("Qual será sua opção? "))
if op == 1:
    total = valor - .10 * valor
elif op == 2:
    total = valor - .05 * valor
elif op == 3:
    total = valor
    parcela = valor / 2
    print("Sua compra será parcelada em 2x de R$ {:.2f}".format(parcela))
elif op == 4:
    parcelas = int(input("Quantas parcelas "))
    total = (1.025 ** parcelas) * valor
    vparc = total / parcelas
    print("Sua compra será parcelada em {}x de R$ {:.2f}".format(parcelas, vparc))
else:
    total = valor
    print("Opção inválida de pagamento! Tente novamente.")
print("Sua compra de R$ {:.2f}, ficará em R$ {:.2f}".format(valor, total))
