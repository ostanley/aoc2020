def part1(file):
    max_cal = 0
    cal_count = 0
    with open(file, "r") as f:
        for line in f:
            if line == "\n":
                max_cal = max(cal_count, max_cal)
                cal_count = 0
            else:
                cal_count += int(line.strip())
    print(f"The snack elf with the most calories has {max_cal} calories.")


def part2(file):
    cal_count_list = []
    cal_count = 0
    with open(file, "r") as f:
        for line in f:
            if line == "\n":
                cal_count_list.append(cal_count)
                cal_count = 0
            else:
                cal_count += int(line.strip())
    cal_count_list.sort()
    print(
        f"The three snack elves with the most calories have {sum(cal_count_list[-3:])} calories."
    )


if __name__ == "__main__":
    file = "Day01input.txt"
    part1(file)
    part2(file)
