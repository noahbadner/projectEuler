# Noah Badner, 2021
#
# Multiples of 3 or 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Solution: 233168; Runtime: O(N)


def multiples_sum(n, factors):
    """Returns the sum of all multiples of the given factors below the upper bound n"""
    sum_of_multiples = 0
    for i in range(n):
        is_multiple = False
        for factor in factors:
            if i % factor == 0:
                is_multiple = True
                break
        if is_multiple:
            sum_of_multiples += i
    return sum_of_multiples


def main():
    """Main method"""
    print(multiples_sum(1000, (3, 5)))


if __name__ == "__main__":
    main()
