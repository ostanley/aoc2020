import core.reader as reader


def score_item(char):
    shared_item_ord = ord(char)
    if shared_item_ord >= ord("a"):
        # item is lowercase
        return shared_item_ord - ord("a") + 1
    else:
        # item is uppercase
        return shared_item_ord - ord("A") + 27


def compare_rugsack_pockets(line):
    top, bottom = line[: len(line) // 2], line[len(line) // 2 :]
    shared_item = set(top).intersection(set(bottom))
    return score_item(shared_item.pop())


def find_misplaced_badges(line_list):
    shared_chars = set(line_list[0])
    for l in line_list[1:]:
        shared_chars = shared_chars.intersection(set(l))
    return score_item(shared_chars.pop())


if __name__ == "__main__":
    file = "Day03/Day03input.txt"
    print(
        "Part 1: Score of mispacked items",
        reader.read_line(file, compare_rugsack_pockets),
    )
    print(
        "Part 2: Score of missing badges",
        reader.group_lines(file, find_misplaced_badges, interval=3),
    )
