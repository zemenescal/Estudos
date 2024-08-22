from anastruct.fem.system import SystemElements

ss = SystemElements(EA=15000, EI=5000)
# g = 25 * .2 * .6  # kN/m - carga permanente
g = 0
ss.add_element(location=[[0, 0], [1.5,0]], g=g)
ss.add_element(location=[[1.5, 0], [3, 0]], g=g)
ss.add_element(location=[[3, 0], [4.5, 0]], g=g)
ss.add_element(location=[[4.5, 0], [6, 0]], g=g)
ss.add_element(location=[[6, 0], [7.5, 0]], g=g)

ss.add_support_hinged(node_id=1)
ss.add_support_roll(node_id=5, direction=2)
ss.q_load(element_id=1, q=-14)
ss.q_load(element_id=[4, 5], q=-9)
ss.point_load(node_id=3, Fy=-30)
ss.moment_load(node_id=1, Ty=25)

ss.show_structure()
ss.solve()

ss.show_reaction_force()
ss.show_shear_force()
ss.show_axial_force()
ss.show_bending_moment()
print(ss.get_element_results(element_id=2))
ss.show_results()
