from collections import deque
from statistics import median

points_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_table = {")": 1, "]": 2, "}": 3, ">": 4}
match_table = {"{": "}", "[": "]", "(": ")", "<": ">"}


def find_corrupt_score(nav_str: str):
    print(f"Processing {nav_str}")
    count_deque = deque()
    for c in nav_str:
        if c in match_table.keys():
            count_deque.append(c)
        else:
            check_open = count_deque.pop()
            if c != match_table[check_open]:
                print(f"{c} corrupted")
                return points_table[c], None
    return 0, count_deque


def fill_in_line(line_deque: deque):
    score = 0
    while len(line_deque) > 0:
        c = line_deque.pop()
        if c not in match_table.keys():
            line_deque.pop()
        else:
            # need to add bracket
            score = autocomplete_table[match_table[c]] + 5 * score
    return score


if __name__ == "__main__":
    p1_score = 0
    p2_score = []
    with open("Day10input.txt", "r") as f:
        for l in f.readlines():
            score, line_deque = find_corrupt_score(l.strip())
            p1_score += score
            if line_deque:
                p2_score.append(fill_in_line(line_deque))
    p2_score.sort()
    print(f"Corruption score is {p1_score}")
    print(f"Autocorrect score is {median(p2_score)}")
