from typing import List


class Point:
    def __init__(self, pos: List) -> None:
        self.x = pos[0]
        self.y = pos[1]


class Grid:
    def __init__(self) -> None:
        self.points = {}
        self.grid_size = [0, 0]

    def add_point(self, p: Point) -> None:
        if (p.x, p.y) in self.points.keys():
            return
        self.points[(p.x, p.y)] = p
        self.grid_size[0] = max(self.grid_size[0], p.x)
        self.grid_size[1] = max(self.grid_size[1], p.y)

    def print_grid(self) -> None:
        for y in range(self.grid_size[1]):
            line = ""
            for x in range(self.grid_size[0]):
                if (x, y) in self.points:
                    line += "#"
                else:
                    line += " "
            print(line)


def perform_fold(instructions, grid):
    new_grid = Grid()
    dir = instructions[0]
    f = int(instructions[1])
    print(f"Folding {dir} along {f}")
    for p in grid.points.values():
        if dir == "x":
            if p.x < f:
                np = p
            else:
                np = Point([2 * f - p.x, p.y])
        elif dir == "y":
            if p.y < f:
                np = p
            else:
                np = Point([p.x, 2 * f - p.y])
        new_grid.add_point(np)
    if dir == "x":
        new_grid.grid_size = [f, grid.grid_size[1]]
    elif dir == "y":
        new_grid.grid_size = [grid.grid_size[0], f]
    return new_grid


if __name__ == "__main__":
    grid = Grid()
    instructions = []
    with open("Day13input.txt", "r") as f:
        for l in f.readlines():
            if l != "\n" and "fold" not in l:
                p = Point([int(x) for x in l.strip().split(",")])
                grid.add_point(p)
            elif "fold" in l:
                instructions.append((l.strip().split()[-1]).split("="))

    for i in instructions:
        grid = perform_fold(i, grid)
    grid.print_grid()
