import numpy as np

'''
v = np.array([1, 2, 3, 4, ], dtype='int32')
print(v)
print(v.dtype)
print(v.shape)
v.shape = (2, 2)
print(v)'''

'''
v = np.array([1, 2, 3, 4, ],dtype='float64').reshape(2,2)
print(v)'''

'''
v = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, -1)
print(v)'''

'''
v = np.array(range(50)).reshape(2, 5, 5)
print(v)
print('Shape = ', v.shape)
print('Número de dimensões =', v.ndim)
print('Número de elementos= ', v.size)
print('Tensor v = \n', v)'''

'''
v = np.zeros((3, 3))
print('v = \n', v)
v=np.ones((3,3))
print('v = \n', v)
v=np.diag((10,3,5))
print('v(diagonal) = \n', v)'''

'''
v = np.arange(0, 5, 0.5)
u = np.linspace(0, 5, 10)
print('v = ', v)
print('u = ', u)'''

'''
v = np.array(range(50)).reshape(2, 5, 5)
print(v)
print(v.flatten())
v_iter = v.flat
for i in v_iter:
    print(i, end=' ')'''

'''
v=np.arange(16).reshape(1,4,4)
print('v=\n',v)
#print('v[0,0,1] = ',v[0,0,1])'''

'''
x=np.arange(10)
media_x = x.mean()
menor_valor=np.min(x)
arg_max=np.argmax(x)
print('Média = ',media_x)
print('Menor valor =',menor_valor)
print('Arg máximo = ',arg_max)'''

'''
A = np.array([10, 30, 40, 20, 5,6,1,12,0]).reshape(3, 3)
menor = A.min()
menor_colunas = A.min(axis=0)
print('A = \n', A)
print('Menor valor = ', menor)
print('Menor valor em cada coluna = ', menor_colunas)'''

'''
v = np.array([10, 20, 30,10]).reshape(2,2)
u = np.array([1, 2, 3,4]).reshape(2,2)
print(u)
print(v)
w = np.dot(v, u)
print('w = ', w)
# Alternativa abaixo
x = u.dot(v)
print('x = ',x)'''
'''
I = np.eye(5)
print(I)
print()
D = np.diag(np.arange(5))
print(D)
########################
A = np.ones((2, 2))
print(A)
B = 10 * np.ones((2, 2))
print(B)
C = np.dot(A, B)
print(C)
########################
C = A @ B
print(C)'''

'''
import timeit
def produto_interno(u, v):
    prod = 0


    for i in range(u.size):
        prod += u[i] * v[i]

    return prod


u = np.random.rand(10000)
v = np.random.rand(10000)

%timeit produto_interno(u, v)
%timeit np.dot(u, v)
# Tenho que aprender como usar timeit '''

'''
u = np.arange(5)
v = np.exp(u)
print(v)'''

'''
A = np.arange(4).reshape(2,2)
print('Transposta de A =\n', np.transpose(A))
print('Transposta de A = \n', A.T) '''

'''
u = np.array([-1, 2, -3])
v = np.array([True, False, True])
print(u[v])

# Alternativa
print(u[u < 0])

# Juntando uma coisa com a outra
print('u = ', u)
u[u < 0] = 0
print('u = ', u)'''

'''
import numpy.random as rd

v = rd.rand(4,4)
print(v)'''

'''
import numpy.random as rd

rd.seed(1000)
v = rd.rand(1, 4)
print(v,'\n')
rd.seed(1000)
v = rd.rand(1, 4)
print(v)'''

'''
A = np.array([10, 20, 30, 40]).reshape(2, 2)
b = np.array([5, 10])
print('Matriz A = \n', A)
print('Matriz b = \n', b)
x = np.linalg.solve(A, b)
print('A solução do sistema é: ', x)'''

A = np.array([10, 20, 30, 40]).reshape(2, 2)
print(A)
b1 = np.array([5, 10]).reshape(2,1)
print('b1= ',b1)
b2 = np.array([10, 12]).reshape(2,1)
print('b2= ',b2)
b = np.hstack([b1, b2])
print("b =\n", b)
x = np.linalg.solve(A, b)
print("x =\n", x)
