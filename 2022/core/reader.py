def read_line(filename, processor):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            total += processor(line.strip())
    return total


def group_lines(filename, processor, interval=None, break_line=None):
    total = 0
    with open(filename, "r") as f:
        line_group = []
        count = 0
        for line in f:
            if line == break_line:
                total += processor(line_group)
            elif count == interval - 1:
                line_group.append(line)
                total += processor(line_group)
                count = 0
                line_group = []
            else:
                line_group.append(line.strip())
                count += 1
    return total
