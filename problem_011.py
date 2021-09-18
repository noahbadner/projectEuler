# Noah Badner, 2021
#
# Largest product in a grid
# Problem 11
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# [included in resource file]
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in
# the 20×20 grid?
# Solution: 70600674; Runtime: O(N^2)

RESOURCE_FILE_PATH = "resources/problem_011_grid.txt"


def parse_file(file_path):
    """Parses the resource file and returns the given grid as a 2 dimensional array"""
    with open(file_path, 'r') as file:
        ret_array = [line.replace("\n", "").split(" ") for line in file]
        file.close()
    return [[num for num in map(int, ret_array[i])] for i in range(len(ret_array))]


def greatest_horizontal_adjacent_product(n, array_2d):
    """Returns the greatest of the products of n horizontally adjacent numbers in a given 2 dimensional array"""
    greatest_product = 0
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i]) - n + 1):
            temp_product = 1
            for k in range(n):
                temp_product *= array_2d[i][j + k]
            greatest_product = max(greatest_product, temp_product)
    return greatest_product


def greatest_right_diagonal_adjacent_product(n, array_2d):
    """Returns the greatest of the products of n right diagonally adjacent numbers in a given 2 dimensional array"""
    greatest_product = 0
    for i in range(len(array_2d) - n + 1):
        for j in range(len(array_2d[i]) - n + 1):
            temp_product = 1
            for k in range(n):
                temp_product *= array_2d[i + k][j + k]
            greatest_product = max(greatest_product, temp_product)
    return greatest_product


def greatest_left_diagonal_adjacent_product(n, array_2d):
    """Returns the greatest of the products of n left diagonally adjacent numbers in a given 2 dimensional array"""
    greatest_product = 0
    for i in range(len(array_2d) - n + 1):
        for j in range((n - 1), len(array_2d[i])):
            temp_product = 1
            for k in range(n):
                temp_product *= array_2d[i + k][j - k]
            greatest_product = max(greatest_product, temp_product)
    return greatest_product


def greatest_vertical_adjacent_product(n, array_2d):
    """Returns the greatest of the products of n vertically adjacent numbers in a given 2 dimensional array"""
    greatest_product = 0
    for i in range(len(array_2d) - n + 1):
        for j in range(len(array_2d[i])):
            temp_product = 1
            for k in range(n):
                temp_product *= array_2d[i + k][j]
            greatest_product = max(greatest_product, temp_product)
    return greatest_product


def grid_greatest_adjacent_product(n, array_2d):
    """Returns the greatest product of n adjacent numbers at any indices in a given grid"""
    return max(greatest_horizontal_adjacent_product(n, array_2d),
               greatest_left_diagonal_adjacent_product(n, array_2d),
               greatest_right_diagonal_adjacent_product(n, array_2d),
               greatest_vertical_adjacent_product(n, array_2d))


def main():
    """Main method"""
    grid = parse_file(RESOURCE_FILE_PATH)
    print(grid_greatest_adjacent_product(4, grid))


if __name__ == "__main__":
    main()
