# Noah Badner, 2021
#
# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Solution: 906609; Runtime: O(N^2)

def is_palindrome(n):
    """Checks if a given integer is a palindrome (e.g. 9009, 12321) and returns a boolean value"""
    int_string = str(n)
    for i in range(len(int_string)//2):
        if int_string[i] != int_string[-i-1]:  # If a left character does not equal the corresponding right character
            return False
    return True


def main():
    """Main method"""
    largest_palindrome = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            product = i * j
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product
    print(largest_palindrome)


if __name__ == "__main__":
    main()
