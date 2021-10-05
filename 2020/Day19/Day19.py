import re
from itertools import product


def parse_rules(rules):
    rule_dict = {}

    for r in rules:
        rule_list = r.split(": ")
        if re.match('"[a-z]*"', rule_list[1]):
            rule_dict[int(rule_list[0])] = rule_list[1][1:-1]
        elif "|" in rule_list[1]:
            rule_dict[int(rule_list[0])] = [
                x.split(" ") for x in rule_list[1].split(" | ")
            ]
        else:
            rule_dict[int(rule_list[0])] = rule_list[1].split(" ")
    return rule_dict


def search_rules(rule_dict, start_key):
    if len(rule_dict[start_key]) == 1:
        if rule_dict[start_key].isalpha():
            return [rule_dict[start_key]]
        else:
            string_list = []
            for k in rule_dict[start_key]:
                print(k)
                string_list += search_rules(rule_dict, int(k))
            return string_list
    else:
        string_list = [[], []]
        for k in rule_dict[start_key][0]:
            string_list[0] += search_rules(rule_dict, int(k))
        for k in rule_dict[start_key][1]:
            string_list[1] += search_rules(rule_dict, int(k))
        return string_list


def make_strings(string_list):
    strings = [""] * 2 ** (depth(string_list) - 1)
    print(len(strings))


def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def main(file):
    with open(file, "r") as f:
        data = f.read()

    [rules, input] = data.split("\n\n")

    rule_dict = parse_rules(rules.strip().split("\n"))
    print(rule_dict)

    string_list = search_rules(rule_dict, 0)
    print(string_list)
    make_strings(string_list)


if __name__ == "__main__":
    file = "Day19testinput.txt"
    main(file)
