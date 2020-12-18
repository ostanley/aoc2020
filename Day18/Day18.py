
def find_outer_brackets(line, counter):
    bracket_loc = [counter]
    bracket_count = 0
    for i in range(len(line[counter:])+1):
        if line[counter+i] == '(':
            bracket_count += 1
        elif line[counter+i] == ')':
            bracket_count -= 1
        if bracket_count == 0:
            bracket_loc.append(counter+i)
            break
    return bracket_loc


def process_line_p1(line):
    output = 0
    counter = 0
    while counter < len(line):
        if counter == 0:
            if line[counter].isnumeric():
                output = int(line[counter])
                counter += 1
            else:
                bracket_loc = find_outer_brackets(line, counter)
                output += process_line_p1(line[bracket_loc[0]+1:bracket_loc[1]])
                counter += bracket_loc[1]+1
        elif line[counter] == '+' or line[counter] == '*':
            if line[counter+1].isnumeric():
                if line[counter] == '+':
                    output += int(line[counter+1])
                else:
                    output *= int(line[counter+1])
                counter += 2
            elif line[counter+1] == '(':
                bracket_loc = find_outer_brackets(line, counter+1)
                if line[counter] == '+':
                    output += process_line_p1(line[bracket_loc[0]+1:bracket_loc[1]])
                else:
                    output *= process_line_p1(line[bracket_loc[0]+1:bracket_loc[1]])
                counter = bracket_loc[1]+1
    return output

if __name__ == '__main__':
    file = "Day18input.txt"

    homework_sum = 0
    with open(file, 'r') as f:
        for l in f.readlines():
            print(l, process_line_p1(l.strip().replace(" ", "")))
            homework_sum += process_line_p1(l.strip().replace(" ", ""))

    print(f'Sum of input lines: {homework_sum}')
