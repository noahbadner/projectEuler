# Noah Badner, 2021
#
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Solution: 6857; Runtime: O(N^2) + O(N) => O(N^2)


def primes(n):
    """Returns a tuple containing every prime number below the given upper bound n sorted from smallest to largest
       Implementation: Check each number for prime factors, and add to list of primes if there are none
       Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate"""
    primes_list = (2,)
    for i in range(3, int(n), 2):  # Prime numbers greater than 2 must be odd numbers
        for prime_factor in primes_list:
            if i % prime_factor == 0:  # A number cannot be prime if it has a prime factor
                break
            if prime_factor**2 > i:  # A number's largest possible prime factor must be smaller than its square root
                primes_list += (i,)
                break
    return primes_list


def largest_factor(n, potential_factors):
    """Returns the largest factor of n given a list of potential factors"""
    for j in range(len(potential_factors)):
        if n % potential_factors[-j] == 0:  # If the candidate factor is a factor of n
            return potential_factors[-j]


def main():
    """Main method"""
    n = 600851475143
    sqrt_n = n**0.5

    # Extract the largest prime factor of n below the square root of n
    primes_list = primes(sqrt_n)
    print(largest_factor(n, primes_list))


if __name__ == "__main__":
    main()
