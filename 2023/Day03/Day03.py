from core.file_reader import scan_lines
from core.geometry import Point2D
from typing import List


class Number:
    def __init__(self, points: List[Point2D], num: int):
        self.points = points
        self.num = num


def check_neighbours(block, pos):
    point = Point2D(*pos)
    for test_x, test_y in point.yield_neighbours():
        if test_x >= len(block) or test_y >= len(block[test_x]) or test_y < 0:
            continue
        test_val = block[test_x][test_y]
        if test_val is not None and not test_val.isdigit() and test_val != ".":
            return True
    return False


def check_numbers(gear, numbers):
    neighbours = []
    for n in numbers:
        # # heuristic for speed
        if abs(gear.x - n.points[0].x) >= 2:
            continue
        for p in gear.yield_neighbours():
            if p in [(p.x, p.y) for p in n.points]:
                neighbours.append(n)
                break
    if len(neighbours) == 2:
        return int(neighbours[0].num) * int(neighbours[1].num)
    return 0


if __name__ == "__main__":
    file = "Day03input.txt"

    with open(file, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    numbers = []
    gears = []
    for x, block in enumerate(lines):
        check_num = Number([], "")
        valid_number = False
        for y, c in enumerate(lines[x] + "."):
            # need to add . for last character to close out check_num
            if c.isdigit():
                check_num.num += c
                check_num.points.append(Point2D(x, y))
                valid_number |= check_neighbours(lines, (x, y))
            else:
                if len(check_num.num) > 0 and valid_number:
                    numbers.append(check_num)
                check_num = Number([], "")
                valid_number = False

            if c == "*":
                gears.append(Point2D(x, y))

    print("Part 1: Parts number count {}".format(sum([int(n.num) for n in numbers])))

    gear_ratio = 0
    for gear in gears:
        gear_ratio += check_numbers(gear, numbers)

    print("Part 2: Gear ratio sum {}".format(gear_ratio))
