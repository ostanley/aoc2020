def yield_line(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        yield line.strip()


def scan_lines(file, length=3):
    block = [None] * length
    for line in yield_line(file):
        block = [line] + block
        block = block[:-1]
        if block[1] is None:
            continue
        else:
            yield block
    # close block
    yield [None] + block[:-1]
