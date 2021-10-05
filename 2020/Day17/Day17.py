import numpy as np


def update_cube(cube, center):
    if center == 1 and (np.sum(cube[:]) == 3 or np.sum(cube[:]) == 4):
        return 1
    elif center == 1:
        return 0
    elif center == 0 and np.sum(cube[:]) == 3:
        return 1
    else:
        return 0


def conway_dims(input_grid, cycles):
    for c in range(cycles):
        input_grid = np.pad(input_grid, 2)
        new_grid = input_grid.copy()
        for x in range(1, input_grid.shape[0] - 1):
            for y in range(1, input_grid.shape[1] - 1):
                for z in range(1, input_grid.shape[2] - 1):
                    if input_grid.ndim == 4:
                        for w in range(1, input_grid.shape[3] - 1):
                            new_grid[x, y, z, w] = update_cube(
                                input_grid[
                                    x - 1 : x + 2,
                                    y - 1 : y + 2,
                                    z - 1 : z + 2,
                                    w - 1 : w + 2,
                                ],
                                input_grid[x, y, z, w],
                            )
                    elif input_grid.ndim == 3:
                        new_grid[x, y, z] = update_cube(
                            input_grid[x - 1 : x + 2, y - 1 : y + 2, z - 1 : z + 2],
                            input_grid[x, y, z],
                        )
        input_grid = new_grid
    return np.sum(input_grid[:])


def main(file):
    with open(file, "r") as f:
        grid = f.read().strip().split("\n")

    input_grid = []
    for l in grid:
        input_grid.append([0 if c == "." else 1 for c in l.strip()])
    input_grid = np.array(input_grid)

    answer = conway_dims(input_grid[:, :, np.newaxis], 6)
    print(f"{answer} active cubes after 6 rounds")

    answer = conway_dims(input_grid[:, :, np.newaxis, np.newaxis], 6)
    print(f"{answer} active hypercubes after 6 rounds")


if __name__ == "__main__":
    file = "Day17input.txt"
    main(file)
