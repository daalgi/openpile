
from openpile.construct import create_pile, create_mesh
from openpile.compute import lateral_loading
from openpile.utils.plots import connectivity_plot

import matplotlib.pyplot as plt

# create pile
pile = create_pile(kind='Circular', 
                   material='Steel', 
                   top_elevation=0, 
                   pile_sections={'length':[40],'diameter':[2], 'wall thickness':[0.08]})
# create mesh
mesh = create_mesh(pile=pile, coarseness=5)

# create point load
# mesh.set_support(elevation=-10, )
mesh.set_support(elevation=-0, Tx = True, Ty =True)
mesh.set_support(elevation=-30, Ty = True)

mesh.set_pointload(elevation=-15,Mz=-200)
mesh.set_pointload(elevation=-20,Py=200)
mesh.set_pointload(elevation=-25,Px=100)
u, f= lateral_loading(mesh)

fig = connectivity_plot(mesh)
plt.show()