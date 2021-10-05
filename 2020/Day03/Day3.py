if __name__ == "__main__":

    # Part 1
    f = open("Day3input.text", "r")
    target_slope = [3, 1]
    current_coords = [0, 0]
    tree_count = 0
    for line in f:
        if line[current_coords[0]] == "#":
            tree_count += 1
            line = line[: current_coords[0]] + "X" + line[current_coords[0] + 1 :]
        else:
            line = line[: current_coords[0]] + "O" + line[current_coords[0] + 1 :]
        print(line[:-1])
        current_coords = [x + y for x, y in zip(current_coords, target_slope)]
        if current_coords[0] >= len(line) - 1:
            current_coords[0] -= len(line) - 1
    f.close()
    print(tree_count)

    # Part 2
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    prod_tree = 1
    for s in slopes:
        line_number = 0
        tree_count = 0
        current_coords = [0, 0]
        target_slope = s
        f = open("Day3input.text", "r")
        for line in f:
            if line_number != current_coords[1]:
                line_number += 1
                print(line[:-1])
                continue
            if line[current_coords[0]] == "#":
                tree_count += 1
                line = line[: current_coords[0]] + "X" + line[current_coords[0] + 1 :]
            else:
                line = line[: current_coords[0]] + "O" + line[current_coords[0] + 1 :]
            print(line[:-1])
            current_coords = [x + y for x, y in zip(current_coords, target_slope)]
            if current_coords[0] >= len(line) - 1:
                current_coords[0] -= len(line) - 1
            line_number += 1
        prod_tree *= tree_count
        f.close()
        print(prod_tree)
