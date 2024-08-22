import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nos = pd.read_excel('entrada.xlsx', sheet_name='Nós')
barras = pd.read_excel('entrada.xlsx', sheet_name='Barras')

# Acertando os números dos nós e das barras conforme a figura (iniciando em 1)
nos.index += 1
barras.index += 1

# Trocando células vazias por zeros
nos.fillna(0, inplace=True)

plt.figure(1, figsize=(12, 4))
plt.ylim(-1, 5)

# Plotagem dos apoios e das forças
for no in nos.index:
    X, Y, RX, RY, Fx, Fy = nos.loc[no]

    # Se RX restrito aplica sobre gl de X
    if RX == 1:
        plt.scatter(X, Y, 400, marker=5, zorder=-2, color='red')
    if RY == 1:
        plt.scatter(X, Y, 400, marker=6, zorder=-2, color='red')

    if Fx > 0:
        plt.arrow(X - 1.5, Y, 1, 0, width=0.05, color='k')
        plt.text(X - 1.5, Y, f'{Fx / 1000}kN', va='bottom')
    if Fx < 0:
        plt.arrow(X + 1.5, Y, -1, 0, width=0.05, color='k')
        plt.text(X + .5, Y, f'{Fx / 1000}kN', va='bottom')
    if Fy > 0:
        plt.arrow(X, Y - 1.5, 0, 1, width=0.05, color='k')
        plt.text(X, Y, f'{Fy / 1000}kN', va='bottom', rotation=90)
    if Fy < 0:
        plt.arrow(X, Y + 1.5, 0, -1, width=0.05, color='k')
        plt.text(X, Y + .5, f'{Fy / 1000}kN', ha='right', rotation=90)

# Plotagem das barras
for barra in barras.index:
    # Vamos passar os nós para as variáveis N1 e N2
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Agora vamos acessar as coordendas de cada um dos nós
    x1, y1 = nos.loc[N1, ['X', 'Y']]
    x2, y2 = nos.loc[N2, ['X', 'Y']]
    y = [y1, y2]
    x = [x1, x2]

    plt.plot(x, y, 'green')
    plt.scatter(x, y, s=80, marker='o', color='black')
    plt.grid(True)
plt.show()

# Criação de listas vazias para armazenar as variáves
Ls = []
sens = []
coss = []

for barra in barras.index:
    # Vamos passar os nós para as variáveis N1 e N2
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Agora vamos acessar as coordendas de cada um dos nós
    x1, y1 = nos.loc[N1, ['X', 'Y']]
    x2, y2 = nos.loc[N2, ['X', 'Y']]

    # O comprimento da barra é dado pelo teorema de Pitagoras
    Lx = x2 - x1
    Ly = y2 - y1
    L = np.sqrt(Lx ** 2 + Ly ** 2)

    # Os cossenos diretores são então:
    sen = Ly / L
    cos = Lx / L

    # Inserindo nas listas
    Ls.append(L)
    sens.append(sen)
    coss.append(cos)

# Agora que saimos do loop vamos inserir no DataFrame
barras['L'] = Ls
barras['sen'] = sens
barras['cos'] = coss

maxgl = 2 * len(nos)
K = np.zeros([maxgl, maxgl])

for barra in barras.index:
    # Vamos importar as propriedades necessárias para construção da matriz local e da matriz de rotação
    L = barras.loc[barra, 'L']
    sen = barras.loc[barra, 'sen']
    cos = barras.loc[barra, 'cos']
    A = barras.loc[barra, 'A']
    E = barras.loc[barra, 'E']
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Matriz de rigidez no sistema local
    Kl = E * A / L * np.array([[1, 0, -1, 0],
                               [0, 0, 0, 0],
                               [-1, 0, 1, 0],
                               [0, 0, 0, 0]])

    # Matriz de rotação
    Mrot = np.array([[cos, sen, 0, 0],
                     [-sen, cos, 0, 0],
                     [0, 0, cos, sen],
                     [0, 0, -sen, cos]])

    # Rotação da matriz de coordenadas locais para globais
    Klr = np.dot(np.dot(Mrot.T, Kl), Mrot)

    # Cálculo dos graus de liberdade
    gl1 = 2 * N1 - 1
    gl2 = 2 * N1
    gl3 = 2 * N2 - 1
    gl4 = 2 * N2

    # Aloca a matriz local na matriz global
    # Lembrando as propriedades das listas do Python!
    K[gl1 - 1:gl2, gl1 - 1:gl2] += Klr[0:2, 0:2]
    K[gl3 - 1:gl4, gl1 - 1:gl2] += Klr[2:4, 0:2]
    K[gl1 - 1:gl2, gl3 - 1:gl4] += Klr[0:2, 2:4]
    K[gl3 - 1:gl4, gl3 - 1:gl4] += Klr[2:4, 2:4]

Kcompleta = K.copy()  # Alocando a matriz em outro espaço de memória

for no in nos.index:
    RX, RY = nos.loc[no, ['RX', 'RY']]
    # Se RX restrito aplica sobre gl de X
    if RX == 1:
        gl = 2 * no - 1
        K[:, gl - 1] = 0
        K[gl - 1, :] = 0
        K[gl - 1, gl - 1] = 1
        print(f'Aplicando restrição horizontal no nó {no}.')

    if RY == 1:
        gl = 2 * no
        K[:, gl - 1] = 0
        K[gl - 1, :] = 0
        K[gl - 1, gl - 1] = 1
        print(f'Aplicando restrição vertical no nó {no}.')

F = np.zeros(maxgl)
for no in nos.index:
    FX, FY = nos.loc[no, ['FX', 'FY']]
    gl1 = 2 * no - 1
    gl2 = 2 * no
    F[gl1 - 1] = FX
    F[gl2 - 1] = FY
U = np.linalg.solve(K, F)

e = 1000
for barra in barras.index:
    # Vamos passar os nós para as variáveis N1 e N2
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Agora vamos acessar as coordendas de cada um dos nós
    x1, y1 = nos.loc[N1, ['X', 'Y']]
    x2, y2 = nos.loc[N2, ['X', 'Y']]

    dx = np.array([U[2 * N1 - 2], U[2 * N2 - 2]])
    dy = np.array([U[2 * N1 - 1], U[2 * N2 - 1]])
    y = [y1, y2]
    x = [x1, x2]
    plt.figure(1, figsize=(12, 4))
    plt.plot(x, y, 'g:')
    plt.plot(x + dx * e, y + dy * e, 'black')
    plt.scatter(x + dx * e, y + dy * e, s=80, marker='o', color='black')
    plt.grid(True)
_ = plt.title('Treliça deformada')
plt.show()

R = np.dot(Kcompleta, U)
# print(R)

plt.figure(1, figsize=(12, 4))
plt.xlim(-2, 15)
plt.ylim(-1, 5)

# Plotagem dos apoios e das forças
for no in nos.index:
    X, Y, RX, RY = nos.loc[no, ['X', 'Y', 'RX', 'RY']]

    gl1 = 2 * no - 1
    gl2 = 2 * no
    Fx = R[gl1 - 1]
    Fy = R[gl2 - 1]

    # Se RX restrito aplica sobre gl de X
    if RX == 1:
        plt.arrow(X - 1.5, Y, 1, 0, width=0.05, color='k')
        plt.text(X - 1.5, Y, f'{Fx / 1000 :.2f}kN', va='bottom')
    if RY == 1:
        plt.arrow(X, Y, 0, 1, width=0.05, color='k')
        plt.text(X + 0.2, Y + 0.8, f'{Fy / 1000 :.2f}kN', va='bottom')

# Plotagem das barras
for barra in barras.index:
    # Vamos passar os nós para as variáveis N1 e N2
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Agora vamos acessar as coordendas de cada um dos nós
    x1, y1 = nos.loc[N1, ['X', 'Y']]
    x2, y2 = nos.loc[N2, ['X', 'Y']]
    y = [y1, y2]
    x = [x1, x2]

    plt.plot(x, y, 'black')
    plt.scatter(x, y, s=80, marker='o', color='black')
plt.show()

Esf = []

for barra in barras.index:
    # Vamos importar as propriedades necessárias para construção da matriz local e da matriz de rotação
    L = barras.loc[barra, 'L']
    sen = barras.loc[barra, 'sen']
    cos = barras.loc[barra, 'cos']
    A = barras.loc[barra, 'A']
    E = barras.loc[barra, 'E']
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']

    # Matriz de rigidez no sistema local
    Kl = E * A / L * np.array([[1, 0, -1, 0],
                               [0, 0, 0, 0],
                               [-1, 0, 1, 0],
                               [0, 0, 0, 0]])

    # Matriz de rotação
    Mrot = np.array([[cos, sen, 0, 0],
                     [-sen, cos, 0, 0],
                     [0, 0, cos, sen],
                     [0, 0, -sen, cos]])
    # Recebendo os deslocamentos referentes ao elemento em análise
    Ul = np.zeros(4)
    Ul[0] = U[2 * N1 - 2]
    Ul[1] = U[2 * N1 - 1]
    Ul[2] = U[2 * N2 - 2]
    Ul[3] = U[2 * N2 - 1]

    # Realizando o equilíbrio local

    F = np.dot(Kl, np.dot(Mrot, Ul))

    # Salvando o terceiro valor do vetor de forças por convenção de sinais.
    Esf.append(F[2])

for barra in barras.index:
    # Vamos passar os nós para as variáveis N1 e N2
    N1 = barras.loc[barra, 'N1']
    N2 = barras.loc[barra, 'N2']
    ax = Esf[barra - 1]
    cos = barras.loc[barra, 'cos']
    sen = barras.loc[barra, 'sen']
    tg = sen / cos
    # Agora vamos acessar as coordendas de cada um dos nós
    x1, y1 = nos.loc[N1, ['X', 'Y']]
    x2, y2 = nos.loc[N2, ['X', 'Y']]
    y = [y1, y2]
    x = [x1, x2]

    plt.figure(1, figsize=(18, 4.5))
    if ax > 0:
        cor = 'r'
    elif ax == 0:
        cor = 'k'
    else:
        cor = 'b'
    plt.plot(x, y, cor, zorder=-1)

    plt.text(np.mean(x), np.mean(y), f'{ax / 1000 :.2f}kN', rotation=180 * np.arctan(tg) / np.pi,
             horizontalalignment='center',
             verticalalignment='center',
             size=16,
             weight='bold')

    plt.scatter(x, y, s=80, marker='o', color='black')

_ = plt.title('Esforços atuantes')
plt.show()
