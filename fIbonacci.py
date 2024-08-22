
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    n = int(input("Digite o número de termos da série de Fibonacci: "))
    for a in range(n):
        print(fib(a) ,end=" ")

if __name__ == "__main__":
    main()
