def find_outer_brackets(line, counter):
    bracket_loc = [counter]
    bracket_count = 0
    for i in range(len(line[counter:]) + 1):
        if line[counter + i] == "(":
            bracket_count += 1
        elif line[counter + i] == ")":
            bracket_count -= 1
        if bracket_count == 0:
            bracket_loc.append(counter + i)
            break
    return bracket_loc


def get_left_num(line, i, func):
    if line[i - 1] not in ops:
        left_num = int(line[i - 1])
        del line[i - 1]
    elif line[i - 1] == ")":
        bkwd_bracket_loc = find_outer_brackets(line.copy()[::-1], len(line) - i)
        left_bracket_loc = [0, 0]
        left_bracket_loc[0] = len(line) - bkwd_bracket_loc[1] - 1
        left_bracket_loc[1] = len(line) - bkwd_bracket_loc[0] - 1
        left_num = func(line[left_bracket_loc[0] + 1 : left_bracket_loc[1]], func)
        del line[left_bracket_loc[0] : left_bracket_loc[1] + 1]
        i = i - (left_bracket_loc[1] - left_bracket_loc[0])
    return left_num, i


def get_right_num(line, i, func):
    if line[i + 1] not in ops:
        right_num = int(line[i + 1])
        del line[i + 1]
    elif line[i + 1] == "(":
        right_bracket_loc = find_outer_brackets(line, i + 1)
        right_num = func(line[right_bracket_loc[0] + 1 : right_bracket_loc[1]], func)
        del line[right_bracket_loc[0] : right_bracket_loc[1] + 1]
    return right_num, i


def process_line_p1(line, func):
    i = 0
    ops = ["+", "*", "(", ")"]
    current_line = line.copy()
    while i < len(line):
        if i == 0 and line[i] == "(":
            bracket_loc = find_outer_brackets(line, i)
            line[i] = func(line[bracket_loc[0] + 1 : bracket_loc[1]], func)
            del line[bracket_loc[0] + 1 : bracket_loc[1] + 1]
            i += 1
        elif line[i] == "+" or line[i] == "*":
            right_num, i = get_right_num(line, i, func)
            left_num, i = get_left_num(line, i, func)
            if line[i - 1] == "+":
                line[i - 1] = right_num + left_num
            else:
                line[i - 1] = right_num * left_num
            if len(line) == 1:
                return line[0]
        else:
            i += 1
    return line[0]


def process_line_p2(line, func):
    i = 0
    ops = ["+", "*", "(", ")"]
    current_line = line.copy()
    while i < len(line):
        if i == 0 and line[i] == "(":
            bracket_loc = find_outer_brackets(line, i)
            line[i] = process_line_p2(line[bracket_loc[0] + 1 : bracket_loc[1]], func)
            del line[bracket_loc[0] + 1 : bracket_loc[1] + 1]
            i += 1
        if line[i] == "+":
            right_num, i = get_right_num(line, i, func)
            left_num, i = get_left_num(line, i, func)
            line[i - 1] = right_num + left_num
        else:
            i += 1
    i = 0
    if len(line) == 1:
        return line[0]
    while i < len(line):
        if line[i] == "*":
            right_num, i = get_right_num(line, i, func)
            left_num, i = get_left_num(line, i, func)
            line[i - 1] = right_num * left_num
        else:
            i += 1
    return line[0]


if __name__ == "__main__":
    file = "Day18input.txt"
    ops = ["*", "+", "(", ")"]

    homework_sum = 0
    homework_sum2 = 0
    with open(file, "r") as f:
        for l in f.readlines():
            new_l = []
            for x in l.strip().split(" "):
                new_l += list(x)
            homework_sum += process_line_p1(new_l.copy(), process_line_p1)
            print(l.strip())
            homework_sum2 += process_line_p2(new_l.copy(), process_line_p2)

    print(f"Sum of input lines: {homework_sum}")
    print(f"Sum of input lines p2: {homework_sum2}")
