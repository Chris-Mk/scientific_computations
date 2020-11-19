import numpy as np
import scipy.linalg as sp


# =============================================================================
# task 01
# =============================================================================


def check_if_symmetric(matrix):
    n, m = matrix.shape

    if n != m:
        return 0
    elif np.array_equal(matrix.T, matrix):
        return 1
    elif np.array_equal(matrix.T, -matrix):
        return -1


A = np.array([[1, 2],
              [4, 5],
              [2, 2]])
print(check_if_symmetric(A))
# alternative
# print(np.array_equal(A, A.T))


B = np.ones([3, 3])
print(check_if_symmetric(B))
# alternative
# print(np.array_equal(B, B.T))

C = np.array([
    [0, 2, -45],
    [-2, 0, -4],
    [45, 4, 0]
])
print(check_if_symmetric(C))


# =============================================================================
# task 02
# =============================================================================

def are_orthogonal(v1, v2):
    scalar_prod = np.dot(v1, v2)

    if scalar_prod == 0:
        return True
    else:
        return False


vector1 = np.array([1, 2, 3])
vector2 = np.array([5, -7, 1])
print(are_orthogonal(vector1, vector2))


# alternative
# print(True if np.dot(vector1, vector2) == 0 else False)

# =============================================================================
# task 03
# =============================================================================

def normalize(vector):
    magnitude = np.sqrt(sum([*vector ** 2]))
    return magnitude
    # return [*vector / magnitude]


v1 = np.array([5, 7, -1])
print(normalize(v1))
print(sp.norm(v1))

v2 = np.array([3, 4])
print(normalize(v2))
print(sp.norm(v2))

# =============================================================================
# task 03
# =============================================================================


