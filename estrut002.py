from anastruct.fem.system import SystemElements

ss = SystemElements(EA=98934.74, EI=2968.04) # fck=30MPa, A=0,20x0,60m
g = 24.52 * .2 * .6  # kN/m - carga permanebte
ss.add_element(location=[5, 0], g=g)
ss.add_element(location=[12, 0], g=g)

ss.add_support_roll(node_id=1, direction=2)
ss.add_support_hinged(node_id=2)
ss.add_support_roll(node_id=3, direction=2)
ss.q_load(element_id=1, q=-2)
ss.q_load(element_id=2, q=-3)
ss.show_structure()
ss.solve()

ss.show_reaction_force()
ss.show_shear_force()
ss.show_axial_force()
ss.show_bending_moment()
print(ss.get_element_results(element_id=2))
ss.show_results()
