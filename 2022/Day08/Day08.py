from dataclasses import dataclass, field
from enum import Enum
from math import prod


class DIRECTIONS(Enum):
    NORTH = [0, -1]
    SOUTH = [0, 1]
    EAST = [1, 0]
    WEST = [-1, 0]


@dataclass
class Tree:
    position: tuple
    height: int
    scenery_list: list = field(default_factory=list)
    visible: bool = False

    def calc_scenery_score(self):
        self.scenery_score = prod(self.scenery_list)
        return self.scenery_score


class Grid2D:
    def __init__(self):
        self.grid = {}

    def add_point(self, coords, val):
        self.grid[coords] = val

    def process_nearby_trees(self, coords):
        for dir in DIRECTIONS:
            visible = True
            neighbour = tuple(x + y for x, y in zip(coords, dir.value))

            # move to edge looking for view blocking tree
            while neighbour in self.grid.keys():
                if self.grid[coords].height <= self.grid[neighbour].height:
                    visible = False
                    break
                else:
                    neighbour = tuple(x + y for x, y in zip(neighbour, dir.value))

            # calculate trees in that direction
            dist = max([abs(x - y) for x, y in zip(coords, neighbour)])
            if neighbour not in self.grid.keys():
                self.grid[coords].scenery_list.append(dist - 1)
            else:
                self.grid[coords].scenery_list.append(dist)

            if not visible:
                continue
            else:
                self.grid[coords].visible = True
        return self.grid[coords].visible

    def count_visible_trees(self):
        count = 0
        for p in self.grid.keys():
            count += int(self.process_nearby_trees(p))
        return count

    def find_best_view(self):
        best_view_score = 0
        for tree in self.grid.values():
            if best_view_score < tree.calc_scenery_score():
                best_view_score = tree.scenery_score
        return best_view_score


def read_trees(filename):
    grid = Grid2D()
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            for j, tree in enumerate(line.strip()):
                grid.add_point((i, j), Tree(position=(i, j), height=tree))
    return grid


if __name__ == "__main__":
    file = "Day08/Day08input.txt"
    grid = read_trees(file)
    print(f"There are {grid.count_visible_trees()} visible trees.")
    print(f"The best view availible is {grid.find_best_view()}.")
