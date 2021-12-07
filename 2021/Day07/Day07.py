from collections import Counter


def calulate_fuel_cost_p1(crab_dict, pos):
    return sum([abs(k - pos) * v for k, v in crab_dict.items()])


def calulate_fuel_cost_p2(crab_dict, pos):
    return sum([sum(range(1, abs(k - pos) + 1)) * v for k, v in crab_dict.items()])


with open("Day07input.txt", "r") as f:
    crab_dict = Counter([int(x) for x in f.readline().strip().split(",")])

    min_fuel_p1 = 10 ** 10
    min_fuel_p2 = 10 ** 10
    pos_to_test = max(crab_dict.keys())
    while pos_to_test > min(crab_dict.keys()):
        min_fuel_p1 = min(calulate_fuel_cost_p1(crab_dict, pos_to_test), min_fuel_p1)
        min_fuel_p2 = min(calulate_fuel_cost_p2(crab_dict, pos_to_test), min_fuel_p2)
        pos_to_test -= 1

    print(f"Guess crab physics minimum fuel: {min_fuel_p2}")
    print(f"Real crab physics minimum fuel: {min_fuel_p2}")
