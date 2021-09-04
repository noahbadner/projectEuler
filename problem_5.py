# Noah Badner, 2021
#
# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Solution: ; Runtime: O()


def main():
    """Main method"""
    smallest_divisible_product = 1
    for i in range(1, 21):
        smallest_divisible_product *= i



if __name__ == "__main__":
    main()
