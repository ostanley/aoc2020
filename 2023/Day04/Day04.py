from core.file_reader import yield_line
import re
from collections import defaultdict


def get_numbers(string):
    return {s for s in set(string.split(" ")) if s != ""}


if __name__ == "__main__":
    file = "Day04input.txt"

    points = 0
    cards = defaultdict(lambda: 1)
    # cards[1] = 1
    pattern = re.compile("Card *(\d+): ([0-9 ]+) [|] ([0-9 ]+)")
    for line in yield_line(file):
        card = pattern.search(line)
        id, winners, numbers = card.groups()
        id = int(id)
        winners = get_numbers(winners)
        numbers = get_numbers(numbers)
        matches = winners.intersection(numbers)

        if len(matches) > 0:
            points += 2 ** (len(matches) - 1)
            for card_copy in range(id + 1, id + len(matches) + 1):
                cards[card_copy] += cards[id]
        if id not in cards.keys():
            cards[id] = 1

    print("Part 1: Points the elf has {}".format(points))
    print("Part 2: Total cards won {}".format(sum(cards.values())))
