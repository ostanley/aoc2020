def parse_and_exec(line):
    line = line.split(' ')
    if line[0] == 'acc':
        return int(line[1]), 1
    elif line[0] == 'nop':
        return 0, 1
    elif line[0] == 'jmp':
        return 0, int(line[1])


def boot_game(lines):
    accumulator = 0
    line_touched = [False] * len(lines)
    line_to_exec = 0
    terminated = False

    while not line_touched[line_to_exec]:
        line_touched[line_to_exec] = True
        accumulator_change, line_change = parse_and_exec(lines[line_to_exec].strip())
        accumulator += accumulator_change
        line_to_exec += line_change
        # print(f'Line is at {line_to_exec-line_change} and going to {line_to_exec}')
        # print(f'Accumulator is at {accumulator}')
        if line_to_exec == len(lines):
            print(f'Program terminated with {accumulator} as final sum')
            terminated = True
            break
    if not terminated:
        print(f'Hit infinite loop, final accumlator value: {accumulator}')
    return terminated


def part1():
    with open('Day8input.txt', 'r') as f:
        lines = f.readlines()

    boot_game(lines)


def part2():
    with open('Day8input.txt', 'r') as f:
        lines = f.readlines()

    switches = [True if 'nop' in s or 'jmp' in s else False for s in lines]

    for s in range(len(switches)):
        if switches[s]:
            newlines = lines.copy()
            if newlines[s][0:3] == 'jmp':
                newlines[s] = newlines[s].replace('jmp', 'nop')
            else:
                newlines[s] = newlines[s].replace('nop', 'jmp')
            terminated = boot_game(newlines)
            if terminated:
                break


if __name__ == '__main__':
    part1()
    part2()
