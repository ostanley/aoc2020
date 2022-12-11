from math import prod
from core.reader import group_lines


def reducer_p1(x, magic_divisor):
    return x // 3


def reducer_p2(x, magic_divisor):
    return x % magic_divisor


class Monkey:
    def __init__(self, id, items, operation, divisor, true_target, false_target):
        self.id = id
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true_target = true_target
        self.false_target = false_target
        self.item_count = 0

    def inspect_items(self, monkey_dict, reducer=reducer_p1, magic_divisor=0):
        for i in self.items:
            i = reducer(self.operation(i), magic_divisor)
            if i % self.divisor == 0:
                monkey_dict[self.true_target].items.append(i)
            else:
                monkey_dict[self.false_target].items.append(i)
            self.item_count += 1
        self.items = []
        return


def parse_monkey(line_group):
    for l in line_group:
        if "Monkey" in l:
            id = int(l.split(" ")[-1][:-1])
        elif "Starting items" in l:
            item_string = l.split(":")[-1]
            if "," in item_string:
                items = [int(i) for i in item_string.split(", ")]
            else:
                items = [int(item_string)]
        elif "Operation" in l:
            equation = l.split("=")[-1].split(" ")
            if equation == ["", "old", "*", "old"]:
                operation = lambda x: x ** 2
            elif "+" in equation:
                operation = lambda x: x + int(equation[-1])
            elif "*" in equation:
                operation = lambda x: x * int(equation[-1])
        elif "Test" in l:
            divisor = int(l.split(" ")[-1])
        elif "If true: throw to monkey" in l:
            true_target = int(l.split(" ")[-1])
        elif "If false: throw to monkey" in l:
            false_target = int(l.split(" ")[-1])

    return [Monkey(id, items, operation, divisor, true_target, false_target)]


if __name__ == "__main__":
    file = "Day11/Day11input.txt"
    monkey_dict = {
        m.id: m
        for m in group_lines(
            file, parse_monkey, break_line="\n", interval=100000, total=[]
        )
    }
    print("Starting items: ", {m.id: m.items for m in monkey_dict.values()})
    steps = 20
    for step in range(steps):
        for monkey_id in range(len(monkey_dict.keys())):
            monkey_dict[monkey_id].inspect_items(monkey_dict)
    print(f"After {steps} steps: ", {m.id: m.items for m in monkey_dict.values()})
    item_count = [m.item_count for m in monkey_dict.values()]
    item_count.sort(reverse=True)
    print(f"Highest two items count after {steps} steps: ", prod(item_count[:2]))

    monkey_dict = {
        m.id: m
        for m in group_lines(
            file, parse_monkey, break_line="\n", interval=100000, total=[]
        )
    }
    print("Starting items: ", {m.id: m.items for m in monkey_dict.values()})
    steps = 10000
    for step in range(steps):
        if step % 5000 == 0:
            print("on step ", step)
            print(
                f"After {steps} steps: ", {m.id: m.items for m in monkey_dict.values()}
            )
        for monkey_id in range(len(monkey_dict.keys())):
            monkey_dict[monkey_id].inspect_items(
                monkey_dict, reducer_p2, prod(m.divisor for m in monkey_dict.values())
            )
    print(f"After {steps} steps: ", {m.id: m.items for m in monkey_dict.values()})
    item_count = [m.item_count for m in monkey_dict.values()]
    item_count.sort(reverse=True)
    print(f"Highest two items count after {steps} steps: ", prod(item_count[:2]))
