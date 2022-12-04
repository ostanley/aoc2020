from core.reader import read_line


def make_assignment_set(section_boarder):
    return set(range(int(section_boarder[0]), int(section_boarder[1]) + 1))


def check_section_duplication(line):
    [s1, s2] = [make_assignment_set(x.split("-")) for x in line.split(",")]
    if s1.difference(s2) == set() or s2.difference(s1) == set():
        return 1
    else:
        return 0


def check_section_overlap(line):
    [s1, s2] = [make_assignment_set(x.split("-")) for x in line.split(",")]
    if len(s1.intersection(s2)) > 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    file = "Day04/Day04input.txt"
    print(
        "Part 1: Elves assigned section duplication",
        read_line(file, check_section_duplication),
    )
    print(
        "Part 2: Elves assigned section overlap",
        read_line(file, check_section_overlap),
    )
