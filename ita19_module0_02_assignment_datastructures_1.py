"""Data structures
Using faces.obj
Define a function for traversing the mesh from boundary to boundary in a "straight" line.
Visualise the result.
"""

import os
import compas
import random

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

plotter = MeshPlotter(mesh, figsize=(16, 10))

# draw border vertices
plotter.draw_vertices(
    keys=list(mesh.vertices_on_boundary()),
    facecolor=(0, 255, 0))

# function
def straight_line_through_quad_mesh(vertex_key):
    """ Draws a straight line through a quad mesh and visualizes this
    """

    line_list = []
    line_list.append(vertex_key)

    nbrs = mesh.vertex_neighbors(vertex_key, ordered = True)
    test_vertex = vertex_key
    for nbr in nbrs:
        if mesh.vertex_degree(nbr) == 4:
            old_vertex = test_vertex
            test_vertex = nbr
            break

    while True:
        line_list.append(test_vertex)
        if mesh.vertex_degree(test_vertex) != 4:
            print("Break")
            break
        nbrs = mesh.vertex_neighbors(test_vertex, ordered = True)
        index = nbrs.index(old_vertex)
        old_vertex = test_vertex
        test_vertex = nbrs[index - 2]

    plotter.draw_vertices(
        radius = 0.2,
        keys=line_list,
        text='key', 
        facecolor=(255,0,0))

    print(line_list)

    plotter.draw_edges()

    plotter.draw_faces()

    plotter.show()

# get vertices on boundary but not on corner
vertices_degree_3 = []
for key in mesh.vertices():
    if mesh.vertex_degree(key) == 3:
        vertices_degree_3.append(key)

# pick a random vertex from the boundary vertices
random_start_vertex = random.choice(vertices_degree_3)

straight_line_through_quad_mesh(random_start_vertex)