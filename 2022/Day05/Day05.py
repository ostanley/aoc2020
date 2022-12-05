import core.reader as reader
import re


def build_stacks(line_group):
    # reverse list so index at top
    line_group = line_group[::-1]
    stack_dict = {}
    for i, c in enumerate(line_group[0]):
        if c == " " or c == "\n":
            continue
        else:  # found a stack
            stack_dict[int(c)] = []
            for l in line_group[1:]:
                if l[i] != " ":
                    stack_dict[int(c)].append(l[i])
    return stack_dict


def crane_stacker_9000(stacks, line):
    p = re.compile(r"\d+")
    n, start, stop = [int(x) for x in p.findall(line)]
    stacks[stop] += stacks[start][-n:][::-1]
    stacks[start] = stacks[start][:-n]
    return stacks


def crane_stacker_9001(stacks, line):
    p = re.compile(r"\d+")
    n, start, stop = [int(x) for x in p.findall(line)]
    stacks[stop] += stacks[start][-n:]
    stacks[start] = stacks[start][:-n]
    return stacks


def parse_file(filename, crane_stacker):
    with open(filename, "r") as f:
        line_group = []
        for line in f:
            if line == "\n":
                stacks = build_stacks(line_group)
            elif "move" in line:
                stacks = crane_stacker(stacks, line)
            else:
                line_group.append(line)
    return "".join([stacks[i][-1] for i in range(1, len(stacks) + 1)])


if __name__ == "__main__":
    file = "Day05/Day05input.txt"
    print("Part 1: Crane stacker 9000", parse_file(file, crane_stacker_9000))
    print("Part 2: Crane stacker 9001", parse_file(file, crane_stacker_9001))
