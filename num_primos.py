# Lista os números primos entre 1 e n
# 28/09/22

def primo(n):
    for val in range(2, n):
        if n % val == 0:
            return False

    return True


def exibe():
    n = int(input('Exibir primos até o número: '))
    for val in range(2, n + 1):
        if primo(val):
            print(val, end = '  ')


while True:
    exibe()