# Noah Badner, 2021
#
# Power digit sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# Solution: 1366; Runtime: O(N)

def sum_of_digits(n):
    """Returns the sum of each individual digit in a given integer n"""
    return sum(int(c) for c in str(n))


def main():
    """Main method"""
    print(sum_of_digits(2**1000))


if __name__ == "__main__":
    main()
