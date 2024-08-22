#"""
def fib(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b

for x in fib(10):
    print(x, end=' ')
print()

#"""
"""

for val in range(1, 11):
    eh_par = "Par" if val % 2 == 0 else "Ímpar"
    print(val, eh_par, sep=' = ')
"""