from core.file_reader import yield_line, split_line
from collections import defaultdict
import numpy as np

if __name__ == "__main__":
    file = "Day02input.txt"

    bag_size = {"red": 12, "green": 13, "blue": 14}
    valid_games = []
    for line in yield_line(file):
        game, pulls = line.split(": ")
        valid = True
        for pull in pulls.split("; "):
            for balls in pull.split(", "):
                count, colour = balls.split(" ")
                if int(count) > bag_size[colour]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_games.append(int(game.split(" ")[-1]))

    print("Part 1: valid game count: {}".format(sum(valid_games)))

    game_power = []
    for line in yield_line(file):
        game, pulls = line.split(": ")
        min_count = defaultdict(lambda: 0)
        for pull in pulls.split("; "):
            for balls in pull.split(", "):
                count, colour = balls.split(" ")
                min_count[colour] = max(min_count[colour], int(count))
        game_power.append(np.prod(min_count.values()))

    print("Part 2: game power sum: {}".format(sum(game_power)))
