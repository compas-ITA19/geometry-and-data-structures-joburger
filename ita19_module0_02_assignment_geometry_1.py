from compas.geometry import cross_vectors
from compas.geometry import normalize_vectors

def orthonormal_from_two_vectors(vect1, vect2):
    """ Returns the three orthonormal vectors from a set of two vectors
    """

    cross = cross_vectors(vect1, vect2)
    orthonormal_vects = normalize_vectors([vect1, vect2, cross])

    return(orthonormal_vects)

