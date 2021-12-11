from enum import Enum
from typing import Tuple, List
from collections import deque


class Neighbours(Enum):
    UP = [0, 1]
    DOWN = [0, -1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    UP_RIGHT = [1, 1]
    DOWN_LEFT = [-1, -1]
    UP_LEFT = [-1, 1]
    DOWN_RIGHT = [1, -1]


class Point:
    def __init__(self, pos: Tuple, energy: int, flashed: bool = False) -> None:
        self.pos = pos
        self.energy = energy
        self.flashed = flashed
        self.neighbours = []
        for e in Neighbours:
            neighbour = [p + n for p, n in zip(self.pos, e.value)]
            if 0 <= neighbour[0] < 10 and 0 <= neighbour[1] < 10:
                self.neighbours.append(tuple(neighbour))

    def __eq__(self, other):
        return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1]


class Grid:
    def __init__(self) -> None:
        self.points = {}
        self.flash = set()

    def add_to_point(self, point: Point):
        point.energy += 1
        if point.energy > 9:
            self.flash.add(tuple(point.pos))

    def flash_points(self):
        flash_count = 0
        while len(self.flash) > 0:
            # pop point from list
            point = self.points[self.flash.pop()]

            # flash point
            point.flashed = True
            flash_count += 1

            # if neighbours should flash add to queue
            for n in point.neighbours:
                self.points[n].energy += 1
                if self.points[n].energy > 9 and not self.points[n].flashed:
                    self.flash.add(self.points[n].pos)
        return flash_count

    def reset_point(self, point):
        if point.flashed:
            point.flashed = False
            point.energy = 0
            return 1
        else:
            return 0

    def display_grid(self):
        for y in range(10):
            line = ""
            for x in range(10):
                line += str(self.points[(x, y)].energy)
            print(line)


if __name__ == "__main__":
    with open("Day11input.txt", "r") as f:
        grid_input = f.readlines()

    grid_input = [list(map(int, l.strip())) for l in grid_input]
    grid = Grid()
    for x in range(10):
        for y in range(10):
            grid.points[(x, y)] = Point(pos=(x, y), energy=grid_input[y][x])

    steps = 10000
    flashes = 0
    for s in range(steps):
        [grid.add_to_point(p) for p in grid.points.values()]
        flashes += grid.flash_points()
        if sum([grid.reset_point(p) for p in grid.points.values()]) == 100:
            print(f"Synchronized at: {s+1}")
            grid.display_grid()
            print(s + 1, flashes)
            break
        grid.display_grid()
