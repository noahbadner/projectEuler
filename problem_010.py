# Noah Badner, 2021
#
# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# Solution: 142913828922; Runtime: O(N^2)

def primes(n):
    """Returns a tuple containing every prime number below the given upper bound n sorted from smallest to largest
       Implementation: Check each number for prime factors, and add to list of primes if there are none
       Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate
       Same implementation that was used in the solution to problem 3"""
    primes_list = (2,)
    for i in range(3, int(n), 2):  # Prime numbers greater than 2 must be odd numbers
        for prime_factor in primes_list:
            if i % prime_factor == 0:  # A number cannot be prime if it has a prime factor
                break
            if prime_factor**2 > i:  # A number's largest possible prime factor must be smaller than its square root
                primes_list += (i,)
                break
    return primes_list


def main():
    """Main method"""
    print(sum(primes(2000000)))


if __name__ == "__main__":
    main()
