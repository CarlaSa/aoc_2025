import numpy as np

from helpers import get_map_input, np_color_print, np_repr

test_input ="""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
test_input = np.array([list(t) for t in test_input.strip().split("\n")])
real_input = np.array(get_map_input(4))

def map_values(x):
    temp = np.zeros_like(x, dtype=int)
    temp[x == "@"] = 1
    return temp

test_input = map_values(test_input)
real_input = map_values(real_input)

def convolution(arr, conv_matrix):
    # very specific convolution, not general
    output = np.zeros_like(arr, dtype=int)
    x,y = arr.shape

    n,m = conv_matrix.shape
    arr = np.pad(arr, ((n//2, n//2), (m//2, m//2)), 'constant')

    for i in range(x):
        for j in range(y):
            output[i,j] = np.sum(arr[i:i + n, j:j + m] * conv_matrix)

    return output

def get_removable_paper(input_array):
    convolution_matrix = np.ones((3,3))
    convolution_matrix[1][1] = 0

    has_paper = input_array == 1
    num_surrounding_paper = convolution(input_array, convolution_matrix)
    return has_paper & (num_surrounding_paper < 4)

def task1(input_array):
    can_remove = get_removable_paper(input_array)
    return np.sum(can_remove)

def task2(input_array, debug = False):
    removed_paper = []
    current = input_array

    if debug:
        np_color_print(current)

    while len(removed_paper) == 0 or removed_paper[-1] != 0:
        removable = get_removable_paper(current)
        removed_paper.append(np.sum(removable).item())
        current[removable] = 0
        if debug:
            print("removed paper:", removed_paper[-1])
            temp = current.copy()
            temp[removable] = 2
            np_color_print(temp)

    return sum(removed_paper)


print(task1(test_input))
print(task1(real_input))

print(task2(test_input, debug = True))
print(task2(real_input))

