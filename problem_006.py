# Noah Badner, 2021
#
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#   1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
#   3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Solution: 25164150; Runtime: O(N)

def sum_of_squares(n):
    """Returns the sum of the squares of each natural number up to n"""
    squares_sum = 0
    for i in range(1, n+1):
        squares_sum += i**2
    return squares_sum


def square_of_sum(n):
    """Returns the square of the sum of each natural number up to n"""
    return sum([i for i in range(1, 100+1)])**2


def main():
    """Main method"""
    print(square_of_sum(100) - sum_of_squares(100))


if __name__ == "__main__":
    main()
