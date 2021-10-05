import itertools


def make_alpha_dict(word):
    dict = {}
    for c in word:
        if c not in dict.keys():
            dict[c] = 1
        else:
            dict[c] += 1
    return dict


def test_pwd(line):
    for x, y in itertools.combinations(line, 2):
        match = True
        if len(x) != len(y) or set(x) != set(y):
            match = False
        else:
            freq_x = make_alpha_dict(x)
            freq_y = make_alpha_dict(y)
            for k, v in freq_x.items():
                if freq_x[k] != freq_y[k]:
                    match = False
        if match:
            return False
    return True


if __name__ == "__main__":
    validp1 = 0
    anagrams = []
    with open("Day04input.txt") as f:
        l = f.readline()
        while l:
            if len(set(l.strip().split(" "))) == len(l.strip().split(" ")):
                validp1 += 1
                anagrams.append(l.strip().split())
            l = f.readline()
        print(f"There are {validp1} valid passwords in part 1.")

    validp2 = 0
    for l in anagrams:
        validp2 += test_pwd(l)
    print(f"There are {validp2} valid passwords in part 2.")
