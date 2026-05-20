import pyvista as pv
from pyvista import examples

# or pv.read('path/to/mesh.obj')
mesh = examples.download_aero_bracket()
mesh.plot()