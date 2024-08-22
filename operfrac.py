# Função mdc
def mdc(a, b):
    while b:
        a, b = b, a % b

    return a


class Fraction:

    def __init__(self, cima, baixo):
        self.num = cima
        self.den = baixo

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __show__(self):
        print(self.num + '/' + self.den)

    def __add__(self, other):
        nnum = self.num * other.den + other.num * self.den
        nden = self.den * other.den
        comum = mdc(nnum, nden)

        return Fraction(nnum // comum, nden // comum)

    def __sub__(self, other):
        nnum = self.num * other.den - other.num * self.den
        nden = self.den * other.den
        comum = mdc(nnum, nden)

        return Fraction(nnum // comum, nden // comum)

    def __mul__(self, other):
        nnum = self.num * other.num
        nden = self.den * other.den
        comum = mdc(nnum, nden)

        return Fraction(nnum // comum, nden // comum)

    def __truediv__(self, other):
        nnum = self.num * other.den
        nden = self.den * other.num
        comum = mdc(nnum, nden)

        return Fraction(nnum // comum, nden // comum)

    def __eq__(self, other):
        pri = self.num * other.den
        seg = self.den * other.num

        return pri == seg


# PrincipalF

x = Fraction(1, 5)
y = Fraction(2, 10)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x == y)
