# Noah Badner, 2021
#
# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Solution: 104743; Runtime: O(N^2)

def main():
    n = 10001
    primes = tuple()

    cursor = 2
    while len(primes) < n:
        is_prime = True
        for i in primes:
            if cursor % i == 0:
                is_prime = False
                break
        if is_prime:
            primes += (cursor,)
        cursor += 1
    print(primes[-1])


if __name__ == "__main__":
    main()
