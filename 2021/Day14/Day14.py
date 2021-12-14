from itertools import islice
from collections import Counter


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    "itertools example"
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def grow_polymer(polymer, polymer_rules):
    new_polymer = Counter({})
    for k, v in polymer_rules.items():
        if k in polymer.keys():
            new_polymer["".join([k[0], v])] += polymer[k]
            new_polymer["".join([v, k[1]])] += polymer[k]
    return new_polymer


def count_polymer(polymer):
    freq_dict = Counter({})
    for k, v in polymer.items():
        freq_dict[k[0]] += v
        freq_dict[k[1]] += v
    return freq_dict


if __name__ == "__main__":
    with open("Day14input.txt", "r") as f:
        polymer_string = f.readline().strip()
        polymer = Counter(["".join(x) for x in window(polymer_string, 2)])

        polymer_rules = {}
        for l in f.readlines():
            if l == "\n":
                continue
            k, v = l.strip().split(" -> ")
            polymer_rules[k] = v

    steps = 40
    for s in range(steps):
        polymer = grow_polymer(polymer, polymer_rules)

    polymer_letters = count_polymer(polymer)
    for k, v in polymer_letters.items():
        if k == polymer_string[-1]:
            polymer_letters[k] = (v + 1) / 2
        else:
            polymer_letters[k] = v / 2

    print(sum(polymer_letters.values()))
    print(polymer_letters)
    print(max(polymer_letters.values()) - min(polymer_letters.values()))
