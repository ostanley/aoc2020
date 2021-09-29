def part1compare(i, string_len):
    if i == len(input) - 1:
        j = 0
    else:
        j = i + 1
    return j


def part2compare(i, string_len):
    j = i + string_len / 2
    if j >= string_len:
        j -= string_len
    return int(j)


def run_captcha(input, function):
    sum = 0
    string_len = len(input)
    for i, c in enumerate(input):
        j = function(i, string_len)
        if input[j] == c:
            sum += int(c)
    return sum


if __name__ == "__main__":
    with open("Day01input.txt", "r") as f:
        input = f.readline().strip()

    # input = "123123"
    print(f"Part 1: {run_captcha(input, part1compare)}")
    print(f"Part 2: {run_captcha(input, part2compare)}")
