# Noah Badner, 2021
#
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Solution: 6857; Runtime: O(N^2) + O(N) => O(N^2)


def main():
    """Main method"""
    n = 600851475143
    sqrt_n = n**0.5

    # Calculate prime numbers below the square root of n
    primes = tuple()
    for i in range(2, int(sqrt_n)):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes += (i,)

    # Extract the largest prime factor of n
    for j in range(len(primes)):
        if n % primes[-j] == 0:
            print(primes[-j])
            break


if __name__ == "__main__":
    main()
