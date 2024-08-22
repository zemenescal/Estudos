class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Olá, meu nome é " + self.name + " e tenho " + str(self.age) + " anos.")


n = input('Qual seu nome? ')
id = int(input('Qual a idade? '))
p1 = Person(n, id)
p1.myfunc()
