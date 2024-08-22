from math import pi

E= float(input('Módulo de elasticidade (kN/mm^2): '))
Ix = float(input('Digite o Momento de Inércia (mm^4): '))
Le = float(input('Digite o comprimento de flambagem (mm): '))
print(f'O P crítico é: {((pi**2)*E*Ix)/Le**2:.2f} kN')