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

def main():
    """Main method"""
    n = 100
    natural_numbers = [i for i in range(1, n+1)]

    sum_of_squares = 0
    for j in natural_numbers:
        sum_of_squares += j**2

    square_of_sum = sum(natural_numbers)**2

    difference = square_of_sum - sum_of_squares
    print(difference)


if __name__ == "__main__":
    main()
