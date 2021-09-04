# Noah Badner, 2021
#
# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# Solution: 142913828922; Runtime: O(N^2)

def main():
    """Main method"""
    n = 2000000
    primes = tuple()
    for i in range(2,n):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes += (i,)
    print(sum(primes))


if __name__ == "__main__":
    main()
