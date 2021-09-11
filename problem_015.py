# Noah Badner, 2021
#
# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
# Solution: 137846528820; Runtime: O(N)

def num_of_routes(n):
    """Returns the number of routes possible following the above rules for an nxn grid"""
    solved_shapes_dict = dict()  # Store previously calculated routes per shape to prevent redundant calculations
    return _check_dimensions(n, n, solved_shapes_dict)


def _check_dimensions(x, y, solved_shapes):
    """Helper function to recursively return the  number of routes from a set of dimensions"""
    # print(f"{x}x{y}")
    if (x, y) in solved_shapes.keys():
        return solved_shapes[(x, y)]
    elif (y, x) in solved_shapes.keys():
        return solved_shapes[(y, x)]
    elif x == 1:
        solved_shapes[(x, y)] = y + 1
        return y + 1
    elif y == 1:
        solved_shapes[(x, y)] = x + 1
        return x + 1
    else:
        solved_shapes[(x, y)] = _check_dimensions(x - 1, y, solved_shapes) + _check_dimensions(x, y - 1, solved_shapes)
        return solved_shapes[(x, y)]


def main():
    """Main method"""
    print(num_of_routes(20))


if __name__ == "__main__":
    main()
