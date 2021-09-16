# Noah Badner, 2021
#
# Counting Sundays
# Problem 19
#
# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Solution: 171; Runtime: O(N)

MONTH_NUM_OF_DAYS_DICT = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap_year(year):
    """Returns a boolean value indicating if the given year is a leap year"""
    return year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0)


def first_of_month_sundays():
    """Returns the number of Sundays that fall on the first of the month from 1901-01-01 to 2000-12-31"""
    num_of_fom_sundays = 0
    year, month, day_of_week = 1901, 1, 2  # day_of_week: 0-6, 0 is Sunday
    while year < 2001:
        if day_of_week == 0:
            num_of_fom_sundays += 1
        day_of_week = (day_of_week + MONTH_NUM_OF_DAYS_DICT[month]) % 7
        month += 1
        if month == 13:
            month = 1
            year += 1
    return num_of_fom_sundays


def main():
    """Main method"""
    print(first_of_month_sundays())


if __name__ == "__main__":
    main()
