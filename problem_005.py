# Noah Badner, 2021
#
# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Solution: 232792560; Runtime: O(N^2)


def main():
    """Main method"""
    n = 20
    factors = [i for i in range(1, n+1)]
    while True:
        could_be_smallest_multiple = True
        for j in factors:
            if n % j != 0:
                could_be_smallest_multiple = False
                break
        if could_be_smallest_multiple:
            break
        n += 1
    print(n)


if __name__ == "__main__":
    main()
