from core.file_reader import yield_line
import numpy


def run_race(time, distance):
    win_count = 0
    for i in range(time):
        run_length = i * (time - i)
        if run_length > distance:
            win_count += 1
    return win_count


if __name__ == "__main__":
    file = "Day06input.txt"
    races = {}
    for i, line in enumerate(yield_line(file)):
        key, values = line.split(":")
        races[key] = [int(r) for r in values.split()]

    winning_cases = []
    for t, d in zip(races["Time"], races["Distance"]):
        winning_cases.append(run_race(t, d))
    print("Part 1: {} winning combos".format(numpy.prod(winning_cases)))

    time = int("".join([str(r) for r in races["Time"]]))
    distance = int("".join([str(r) for r in races["Distance"]]))
    print("Part 2: {} ways to win".format(run_race(time, distance)))
