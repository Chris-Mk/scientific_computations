import time as t
import imageio as io
from matplotlib.pyplot import *
from projectHaar.haar_functions import *

img = io.imread('./files/kvinna.jpg', as_gray=True)


def haar_transformation(image):
    image = trim_image(image)
    rows, cols = image.shape

    w = makeW(rows)
    w_inverse = makeW(cols).T

    trans_img = dot(dot(w, image), w_inverse)
    mid_r, mid_c = rows // 2, cols // 2

    A = trans_img[0:mid_r, 0:mid_c]
    B = trans_img[mid_r:rows, 0:mid_c]
    C = trans_img[0:mid_r, mid_c:cols]
    D = trans_img[mid_r:rows, mid_c:cols]

    return A, B, C, D
    # return trans_img


# start_time = t.time()
# img_comp = haar_transformation(img)
# print("Matrix haar=", t.time() - start_time)
# imshow(get_components(img_comp), cmap='gray')
# imshow(inverse_haar_transformation(img_comp), cmap='gray')

# io.imwrite("./files/new_kvinna.jpg", get_components(img_comp))


def direct_haar(image):
    image = trim_image(image)
    rows, cols = image.shape

    for index in range(cols):
        curr_col = image[:, index]
        image[:, index] = destroy_vec(curr_col)

    for index in range(rows):
        curr_row = image[index, :]
        image[index, :] = destroy_vec(curr_row)

    return image

# str_time = t.time()
# direct_haar(img)
# print("Direct haar=", t.time() - str_time)
# imshow(direct_haar(img), cmap='gray')


