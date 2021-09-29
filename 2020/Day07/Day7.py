import re


def parse_rule(line, rule_dict):
    bag_rule = re.split(' bag contain | bags contain | bag, | bags, | bags| bag', line)
    if bag_rule[0] not in rule_dict.keys():
        rule_dict[bag_rule[0]] = []
    for bag in bag_rule[1:-1]:
        if bag == 'no other':
            rule_dict[bag_rule[0]].append([0, bag])
        else:
            bag = bag.split(' ', 1)
            rule_dict[bag_rule[0]].append([int(bag[0]), bag[1]])
    return rule_dict


def find_bag(target_bag, rule_dict, containing_bags):
    for key, value in rule_dict.items():
        for bag in value:
            if bag[1] == target_bag:
                containing_bags.append(key)
                find_bag(key, rule_dict, containing_bags)
    return containing_bags


def count_bags(target_bag, rule_dict, count):
    inner_bag_count = 1  # so that the outer bag is counted
    for bag in rule_dict[target_bag]:
        if bag[0] == 0:
            inner_bag_count = 1
        else:
            inner_bag_count += bag[0]*count_bags(bag[1], rule_dict, count)
    return count+inner_bag_count


def main():
    rules = {}
    with open('Day7input.txt', 'r') as f:
        for l in f:
            rules = parse_rule(l.strip('.\n'), rules)

    bag_list = find_bag('shiny gold', rules, [])
    print(f'Part 1: {len(set(bag_list))} bags can hold the shiny gold bag')

    target_bag = 'shiny gold'
    bag_count = count_bags(target_bag, rules, 0)-1  # to not count the external bag
    print(f'Part 2: The {target_bag} bag must hold {bag_count} bags')


if __name__ == '__main__':
    main()
