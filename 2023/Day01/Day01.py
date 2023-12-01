import re
from core.file_reader import yield_line

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def match_digit(string, case, pos):
    match = re.findall(case, string)[pos]

    if match in numbers.keys():
        return numbers[match]
    else:
        return int(match)


def run_calibration(file, match_string, verbose=False):
    calibration_sum = 0
    for row in yield_line(file):
        calibration = match_digit(row, match_string, 0) * 10 + match_digit(
            row, match_string, -1
        )
        if verbose:
            print(f"{row}: {calibration}")
        calibration_sum += calibration
    return calibration_sum


if __name__ == "__main__":
    file = "Day01input.txt"
    print("Part 1: ", run_calibration(file, "[0-9]"))
    print(
        "Part 2: ",
        run_calibration(
            file,
            "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))",
        ),
    )
