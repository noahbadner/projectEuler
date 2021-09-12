# Noah Badner, 2021
#
# Maximum path sum I
# Problem 18
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#   >3<
#  >7<4
#  2>4<6
# 8 5>9<3
# [included in resource file]
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
# [included in resource file]
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
# is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
# clever method! ;o)
# Solution: 1074; Runtime: O(Nlog(N))

def parse_file(file_path):
    """Parses the input file and return a triangle as a list of rows, each a list of the integers that make them up"""
    ret_list = list()
    with open(file_path, 'r') as file:
        for line in file:
            ret_list.append([int(num) for num in line.split(" ")])
    return ret_list


def max_path_sum(triangle):
    """
    Returns the maximum path sum of a given triangle
    :param list triangle: A triangle nested lists where each list is a row of the triangle
    :return int: The greatest sum of the available paths from the top of a given triangle
    """
    for i in range(len(triangle)-1):
        for j in range(len(triangle[-1-i])-1):
            triangle[-2-i][j] += max(triangle[-1-i][j], triangle[-1-i][j+1])
    return triangle[0][0]


def main():
    """Main method"""
    print(max_path_sum(parse_file("resources/problem_018_triangle.txt")))


if __name__ == "__main__":
    main()
