from compas.geometry import cross_vectors
import numpy as np

def cross_product_from_arrays_python(array1, array2):
    """ Computes the cross product of two arrays of vectors in pure Python
    """
    cross_list = []

    for i in range(len(vect_array1)):
        v1 = array1[i]
        v2 = array2[i]

        cross = cross_vectors(v1,v2)
        cross_list.append(cross)

    return cross_list

def cross_product_from_arrays_numpy(array1, array2):
    """ Computes the cross product of two arrays of vectors using numpy
    """
    cross = np.cross(array1, array2)
    return cross