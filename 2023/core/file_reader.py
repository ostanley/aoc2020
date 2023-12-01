def yield_line(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        yield line.strip()
