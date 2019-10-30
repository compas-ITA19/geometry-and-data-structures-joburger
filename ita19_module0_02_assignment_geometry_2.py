from compas_plotters import Plotter
from compas.geometry import centroid_polygon
from compas.geometry import Vector
from compas.geometry import cross_vectors
from compas.geometry import length_vector

plotter = Plotter()

def get_area_convex_2d_polygon(polygon):
    """ Computes the area of a convex 2d polygon by using cross product
    """

    area = 0

    centroid = centroid_polygon(polygon)
    centroid_vect = Vector(centroid[0], centroid[1], centroid[2])

    for i in range(len(polygon)):
        pt1 = Vector(polygon[i][0], polygon[i][1], polygon[i][2])
        pt2 = Vector(polygon[i-1][0], polygon[i-1][1], polygon[i-1][2])

        vect_side1 = pt1 - centroid_vect
        vect_side2 = pt2 - centroid_vect

        cross = cross_vectors(vect_side1, vect_side2)
        cross_length = length_vector(cross)
        face_area = cross_length / 2

        area += face_area

    print(area)
    return area

polygon = [
    [3.0, 1.0, 0.0],
    [4.0, 2.0, 0.0],
    [3.0, 3.0, 0.0],
    [2.0, 3.0, 0.0],
    [1.0, 2.0, 0.0],
    [2.0, 1.0, 0.0]
]

get_area_convex_2d_polygon(polygon)

plotter.draw_polygons([{'points': polygon}])
plotter.show()