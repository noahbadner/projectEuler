# Noah Badner, 2021
#
# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Solution: 104743; Runtime: O(N^2)

def primes(n):
    """Returns a tuple containing every prime number below the given upper bound n sorted from smallest to largest
       Implementation: Check each number for prime factors, and add to list of primes if there are none
       Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate
       Similar to the implementation in the solution to problem 3"""
    primes_list = (2,)
    cursor = 3
    while len(primes_list) < n:  # Prime numbers greater than 2 must be odd numbers
        for prime_factor in primes_list:
            if cursor % prime_factor == 0:  # A number cannot be prime if it has a prime factor
                break
            if prime_factor**2 > cursor:  # A number's largest prime factor must be smaller than its square root
                primes_list += (cursor,)
                break
        cursor += 1
    return primes_list


def main():
    """Main method"""
    print(primes(10001)[-1])


if __name__ == "__main__":
    main()
