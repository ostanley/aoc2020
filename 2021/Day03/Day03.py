def sum_lines(lines):
    count = [0] * (len(lines[0]) - 1)
    for l in lines:
        count = [x + int(y) for x, y in zip(count, l.strip())]
    return count


def find_majority_lines(lines, match=["1", "0"]):
    bit = 0
    while len(lines) > 1 and bit < len(lines[0]) - 1:
        count = sum_lines(lines)
        if count[bit] >= len(lines) / 2:
            lines = [l for l in lines if l[bit] == match[0]]
        else:
            lines = [l for l in lines if l[bit] == match[1]]
        bit += 1
    return lines


def boolstr_to_int(bool_str):
    return int("".join([str(x) for x in bool_str]), 2)


if __name__ == "__main__":
    with open("Day03input.txt", "r") as f:
        lines = f.readlines()

    count = sum_lines(lines)

    gamma_rate = []
    epsilon_rate = []
    for bit in count:
        if bit >= len(lines) / 2:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    gamma_rate = boolstr_to_int(gamma_rate)
    epsilon_rate = boolstr_to_int(epsilon_rate)

    print(f"Power rating: {gamma_rate * epsilon_rate}")

    oxygen_generator = boolstr_to_int(find_majority_lines(lines))
    co2_generator = boolstr_to_int(find_majority_lines(lines, ["0", "1"]))

    print(f"Life support rating: {co2_generator*oxygen_generator}")
