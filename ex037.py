num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] - Concerter para binário
[ 2 ] - Converter para octal
[ 3 ] - Converter para hexadecimal.''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para binãrio é: {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para hexadecimal é: {hex(num)[2:].upper()}')
else:
    print('Opção inválida. Tente com uma opção válida.')