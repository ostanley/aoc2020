rules = {"A": "X", "B": "Y", "C": "Z"}
scores = {"X": 1, "Y": 2, "Z": 3}
wins_against = {"X": "Z", "Y": "X", "Z": "Y"}
loses_against = {v: k for k, v in wins_against.items()}


def read_line(filename, processor):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            total += processor(line.strip())
    return total


def calc_game(line):
    opponent, you = line.split(" ")
    if rules[opponent] == you:
        return 3 + scores[you]
    elif wins_against[you] == rules[opponent]:
        return 6 + scores[you]
    else:
        return scores[you]


def rig_game(line):
    opponent, goal = line.split(" ")
    if goal == "Y":
        return 3 + scores[rules[opponent]]
    elif goal == "X":
        return 0 + scores[wins_against[rules[opponent]]]
    else:
        return 6 + scores[loses_against[rules[opponent]]]


if __name__ == "__main__":
    filename = "Day02input.txt"
    print(f"Part 1: {read_line(filename, calc_game)}")
    print(f"Part 2: {read_line(filename, rig_game)}")
