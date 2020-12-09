def in_preamble(num_sum, preamble):
    for val in preamble:
        if num_sum-val in preamble:
            return True
    return False


def part1(preamble_length, file):
    with open(file, 'r') as f:
        preamble = []
        for l in f:
            if len(preamble) == preamble_length:
                if not in_preamble(int(l.strip()), preamble):
                    print(f'{int(l.strip())} does not have sum not in preamble')
                    return int(l.strip())
                preamble.pop(0)
            preamble.append(int(l.strip()))


def part2(num, file):
    with open(file, 'r') as f:
        input = [int(l.strip()) for l in f]

    start_index = 0
    sum_end = 0
    contiguous_sum = 0

    while start_index < len(input):
        contiguous_sum += input[sum_end]
        sum_end += 1
        if contiguous_sum == num:
            print(f'found sum string at {start_index} to {sum_end}')
            sum_range = input[start_index:sum_end]
            print(f"ecryption weakness is {min(input[start_index:sum_end])}+"
                  f"{max(input[start_index:sum_end])}="
                  f"{min(input[start_index:sum_end])+max(input[start_index:sum_end])}")
            break
        elif contiguous_sum > num:
            contiguous_sum = 0
            start_index += 1
            sum_end = start_index


if __name__ == '__main__':
    file = 'Day9testinput.txt'
    test_num = part1(5, file)
    part2(test_num, file)
    file = 'Day9input.txt'
    num = part1(25, file)
    part2(num, file)
