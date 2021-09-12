# Noah Badner, 2021
#
# Factorial digit sum
# Problem 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
# Solution: 648; Runtime: O(N)

def factorial(n):
    """Returns the value of n! if n >= 0"""
    if n < 0:
        raise Exception(f"n! for n < 0: n = {n}")
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def digit_sum(n):
    """Returns the sum of the digits in the given integer n"""
    sum_of_digits = 0
    for c in str(n):
        sum_of_digits += int(c)
    return sum_of_digits


def main():
    """Main method"""
    print(digit_sum(factorial(100)))


if __name__ == "__main__":
    main()
