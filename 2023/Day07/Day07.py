from core.file_reader import yield_line
from collections import Counter, defaultdict

# hand order
hand_order = {
    (5,): 0,  # five of a kind
    (4, 1): 1,  # four of a kind
    (3, 2): 2,  # full house
    (3, 1, 1): 3,  # three of a kind
    (2, 2, 1): 4,  # two pair
    (2, 1, 1, 1): 5,  # pair
    (1, 1, 1, 1, 1): 6,
}  # singles

p1_card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
p2_card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def score_hand_rank(hand, p2=False):
    card_counter = Counter(hand)
    if p2 and "J" in hand:
        wilds = card_counter["J"]
        del card_counter["J"]
        if len(card_counter.keys()) == 0:  # JJJJJ case
            card_counter["J"] = wilds
        else:
            card_counter[card_counter.most_common()[0][0]] += wilds
    card_freq = sorted(card_counter.values(), reverse=True)

    return hand_order[tuple(card_freq)]


def sort_card_values(hand_list, p2=False):
    if p2:
        card_order = p2_card_order
    else:
        card_order = p1_card_order
    alphabet_to_card_map = {chr(97 + i): k for i, k in enumerate(card_order)}
    card_to_alphabet_map = {k: chr(97 + i) for i, k in enumerate(card_order)}
    if len(hand_list) == 1:
        return hand_list
    sorted_hand_list = sorted(
        ["".join([card_to_alphabet_map[c] for c in hand]) for hand in hand_list],
    )
    return [
        "".join([alphabet_to_card_map[c] for c in hand]) for hand in sorted_hand_list
    ]


def get_card_rank(file, p2=False):
    hand_rank = defaultdict(lambda: [])
    hand_bid = {}
    for hand, bid in [l.split(" ") for l in yield_line(file)]:
        hand_rank[score_hand_rank(hand, p2)].append(hand)
        hand_bid[hand] = bid

    sorted_hands = []
    for i in sorted(hand_rank.keys()):
        if len(hand_rank[i]) > 0:
            sorted_hands += sort_card_values(hand_rank[i], p2)

    return sum(
        [(i + 1) * int(hand_bid[hand]) for i, hand in enumerate(sorted_hands[::-1])]
    )


if __name__ == "__main__":
    file = "Day07input.txt"

    print("Part 1: {} winnings".format(get_card_rank(file)))
    print("Part 2: {} winnings".format(get_card_rank(file, p2=True)))
