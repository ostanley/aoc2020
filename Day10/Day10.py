import numpy as np
import functools


def part1(file):
    with open(file, 'r') as f:
        input = [int(x.strip()) for x in f]

    input.sort()
    input.insert(0, 0)
    input.insert(len(input), input[-1]+3)
    print(f'sorted list: {input}')

    diffs = np.diff(input)

    print(f'Answer: {sum(diffs == 1)*sum(diffs == 3)}')

    return input, diffs


@functools.lru_cache(maxsize=128)
def part2(input):
    target_list = input[1:4]
    sum = 0
    for i in [1, 2, 3]:
        if input[0]+i in target_list:
            new_index = target_list.index(input[0]+i)+1
            sum += part2(input[new_index:])
    if sum == 0:
        sum = 1
    return sum


if __name__ == '__main__':
    file = 'Day10input.txt'
    input, diffs = part1(file)
    sum = part2(tuple(input))
    print(f'Combos: {sum}')
