from collections import Counter, defaultdict


def breed(fish_dict):
    new_fish_dict = defaultdict(lambda: 0)
    for i in range(0, 9):
        if i in fish_dict.keys() and i - 1 >= 0:
            new_fish_dict[i - 1] += fish_dict[i]
        elif i == 0:
            new_fish_dict[6] += fish_dict[0]
            new_fish_dict[8] += fish_dict[0]
    return new_fish_dict


def run_laternfish_sim(fish_dict, days):
    for _ in range(days):
        fish_dict = breed(fish_dict)
    return sum(fish_dict.values())


with open("Day06input.txt", "r") as f:
    fish_dict = defaultdict(
        lambda: 0, Counter([int(x) for x in f.readline().strip().split(",")])
    )

    print(f"Lanternfish population has grown to: {run_laternfish_sim(fish_dict, 80)}")
    print(f"Lanternfish population has grown to: {run_laternfish_sim(fish_dict, 256)}")
