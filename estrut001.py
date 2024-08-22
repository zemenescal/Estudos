########## AnaStruct ############
#  Viga contínua - peso próprio #
######## 29/11/22  ##############

from anastruct.fem.system import SystemElements


# Dados geométricos da viga
b = 0.20  # em m
h = 0.60  # em m
fck = 25  # em MPa
A = round(b * h, 4)  # em m2
g = round(24.5166 * A, 4)  # kN/m3 * A - peso próprio em kN/m
E = round(.85 * (5600 * fck ** (1 / 2)) * 1e3, 8)  # em kPa (kN/m2)
I = round((b * h ** 3) / 12, 8)  # em m4v

# Impressão dos dados iniciais
print('A=', A, 'm2')
print('Peso próprio= ', g, ' kN/m')
print('E=', E, 'kPa')
print('I=', I, 'm4')
print('EA=', E * A, 'kN')
print('EI=', E * I, 'kNxm2')

ss = SystemElements(EA=E * A, EI=E * I)
ss.add_element(location=[[0, 0], [5, 0]], g=g)
ss.add_element(location=[[5, 0], [12, 0]], g=g)
ss.add_support_hinged(node_id=1)
ss.add_support_hinged(node_id=2)
ss.add_support_roll(node_id=3)
ss.q_load(element_id=1, q=-16)
ss.q_load(element_id=2, q=-6)

ss.solve()
ss.show_structure()

# Resultados no gráfico
ss.show_reaction_force()
ss.show_shear_force()
ss.show_bending_moment()
ss.show_displacement(factor=10e2)
ss.show_results()
