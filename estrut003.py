from anastruct import SystemElements
import numpy as np
ss = SystemElements()
element_type = 'truss'
# Create 2 towers
width = 6
span = 30
k = 5e3
# create triangles
y = np.arange(1, 10) * np.pi
x = np.cos(y) * width * 0.5
x -= x.min()
for length in [0, span]:
    x_left_column = np.ones(y[::2].shape) * x.min() + length
    x_right_column = np.ones(y[::2].shape[0] + 1) * x.max() + length
    # add triangles
    ss.add_element_grid(x + length, y, element_type=element_type)
    # add vertical elements
    ss.add_element_grid(x_left_column, y[::2], element_type=element_type)
    ss.add_element_grid(x_right_column, np.r_[y[0], y[1::2], y[-1]], element_type=element_type)
    ss.add_support_spring(node_id=ss.find_node_id(vertex=[x_left_column[0], y[0]]),translation=2,k=k)
    ss.add_support_spring(node_id=ss.find_node_id(vertex=[x_right_column[0], y[0]]),translation=2,k=k)
# add top girder
ss.add_element_grid([0, width, span, span + width], np.ones(4) * y.max(), EI=10e3)
# Add stability elements at the bottom.
ss.add_truss_element([[0, y.min()], [width, y.min()]])
ss.add_truss_element([[span, y.min()], [span + width, y.min()]])
for el in ss.element_map.values():
    # apply wind load on elements that are vertical
    if np.isclose(np.sin(el.a1), 1):
        ss.q_load(q=1,element_id=el.id,direction='x')
ss.show_structure()
ss.solve()
ss.show_displacement(factor=2)
ss.show_bending_moment()
print(ss.get_element_results(element_id=36)['N'])
