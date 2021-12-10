from dataclasses import dataclass
from typing import Dict, List
from math import prod


@dataclass
class Point:
    pos: List
    neighbours: Dict
    height: int
    grid_size: List
    low_point: bool = True
    in_basin = False

    def get_neighbour(self, dir, grid):
        neighbour = [x + y for x, y in zip(self.pos, dir)]
        if (
            neighbour[0] >= 0
            and neighbour[0] < self.grid_size[0]
            and neighbour[1] >= 0
            and neighbour[1] < self.grid_size[1]
        ):
            self.neighbours[tuple(neighbour)] = grid[neighbour[1]][neighbour[0]]
            return self.neighbours[tuple(neighbour)]
        else:
            return -1


def find_basin(point: Point, point_dict: dict):
    if point.height == 9:
        return []
    else:
        point.in_basin = True
        points_in_basin = [point.pos]
        for n in point.neighbours:
            if not point_dict[n].in_basin:
                points_in_basin += find_basin(point_dict[n], point_dict)
        return points_in_basin


if __name__ == "__main__":
    with open("Day09input.txt", "r") as f:
        grid = f.readlines()

    grid = [list(map(int, l.strip())) for l in grid]

    point_dict = {}
    risk_level = 0
    grid_size = [len(grid[0]), len(grid)]
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    low_points = []
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            point_dict[(x, y)] = Point(
                pos=[x, y], neighbours={}, height=grid[y][x], grid_size=grid_size
            )

            for dir in directions:
                neighbour_height = point_dict[(x, y)].get_neighbour(dir, grid)
                if (neighbour_height <= point_dict[(x, y)].height) and (
                    neighbour_height >= 0
                ):
                    point_dict[(x, y)].low_point = False
            if point_dict[(x, y)].low_point:
                print(
                    f"Position: {point_dict[(x, y)].pos} is a low point with height {point_dict[(x, y)].height} and {len(point_dict[(x, y)].neighbours.keys())} neighbours"
                )
                risk_level += 1 + point_dict[(x, y)].height
                low_points.append(point_dict[(x, y)].pos)

    basin_sizes = []
    for l in low_points:
        basin_sizes.append(len(find_basin(point_dict[tuple(l)], point_dict)))

    basin_sizes.sort(reverse=True)
    print(f"Risk level for this grid is {risk_level}")
    print(f"Product of the top three basins is {prod(basin_sizes[0:3])}")
