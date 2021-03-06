from numpy import *


def make_w(n):
    w = zeros([n, n])
    multi = sqrt(2) / 2
    mid = n // 2

    for i in range(mid):
        j = 2 * i
        w[i, j] = 1
        w[i, j + 1] = 1
        w[mid, j] = -1
        w[mid, j + 1] = 1
        mid += 1
    return w * multi


# def makeW(size):
#     multi = sqrt(2) / 2
#     W = zeros([size, size])
#     c = 0
#     h = int(size / 2)
#     for i in range(size - h):
#         W[i][c] = 1
#         W[i + h][c] = -1
#         c += 1
#         W[i][c] = 1
#         W[i + h][c] = 1
#         c += 1
#     W = W * multi
#     return W


def inverse_haar_transformation(m):
    I = stack_submatrices(m)
    rows, cols = I.shape

    w = make_w(cols)
    w_inverse = make_w(rows).T
    return dot(dot(w_inverse, I), w)


def stack_submatrices(m):
    h1 = hstack([m[0], m[1]])
    h2 = hstack([m[2], m[3]])
    I = vstack([h1, h2])
    return I


def trim_image(image):
    rows, cols = image.shape
    if rows % 2 != 0:
        rows -= 1

    if cols % 2 != 0:
        cols -= 1

    return image[0:rows, 0:cols]


def avg_diff_vec(vec):
    mid = len(vec) // 2
    multi = sqrt(2) / 2
    new_vec = zeros(len(vec))

    for i in range(mid):
        j = 2 * i
        s = vec[j] + vec[j + 1]
        d = vec[j + 1] - vec[j]

        new_vec[i] = s
        new_vec[mid] = d
        mid += 1

    return new_vec * multi
