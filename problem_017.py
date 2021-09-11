# Noah Badner, 2021
#
# Number letter counts
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
# usage.
# Solution: 21124; Runtime: O(N)

# Dictionary constant to facilitate converting integers to written number strings
INT_TO_STRING_DICT = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                      9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                      16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                      40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def int_to_written_number(n):
    """Returns the written representation of a given number in compliance with British English"""
    # Thousands
    if n >= 1000:
        thousands_place = n // 1000
        return int_to_written_number(thousands_place) + " thousand" + \
            (f" {int_to_written_number(n-(thousands_place*1000))}" if n-(thousands_place*1000) != 0 else "")
    # Hundreds
    if n >= 100:
        hundreds_place = n // 100
        return int_to_written_number(hundreds_place) + " hundred" + \
            (f" and {int_to_written_number(n-(hundreds_place*100))}" if n-(hundreds_place*100) != 0 else "")
    # Below 100
    if n < 21:
        return INT_TO_STRING_DICT[n]
    else:
        tens_place = n//10
        return INT_TO_STRING_DICT[tens_place*10] + (f"-{INT_TO_STRING_DICT[n-(tens_place*10)]}" if n % 10 != 0 else "")


def letters_in_string(s):
    """Returns the number of letters in a string"""
    num_letters = 0
    for c in s.lower():
        if c in "abcdefghijklmnopqrstuvwxyz":
            num_letters += 1
    return num_letters


def main():
    """Main method"""
    words_string = ""
    for i in range(1, 1001):
        words_string += f"{int_to_written_number(i)}\n"
    print(letters_in_string(words_string))


if __name__ == "__main__":
    main()
