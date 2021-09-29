import itertools


def part1(arr):
    return max(arr) - min(arr)


def part2(arr):
    for i, j in itertools.combinations(arr, 2):
        if i > j and i % j == 0:
            return int(i / j)
        elif j % i == 0:
            return int(j / i)


def run_checksum(input, function):
    checksum = 0
    for l in input:
        numbers = [int(x) for x in l.strip().split("\t")]
        checksum += function(numbers)
    return checksum


if __name__ == "__main__":
    with open("Day02input.txt") as f:
        input = f.readlines()

    print(run_checksum(input, part1))
    print(run_checksum(input, part2))
