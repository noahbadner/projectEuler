# Noah Badner, 2021
#
# Large sum
# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#   [Attached in resource file]
# Solution: 5537376230; Runtime: O(N)

def parse_file(file_path):
    """Parses the resource file and returns the given list of 50-digit numbers"""
    with open(file_path, 'r') as file:
        ret_list = [int(line.replace("\n", "")) for line in file]
        file.close()
    return ret_list


def main():
    """Main method"""
    print(str(sum(parse_file("resources/problem_013_numbers.txt")))[:10])


if __name__ == "__main__":
    main()
