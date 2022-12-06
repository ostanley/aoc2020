from core.reader import read_line


def find_start_marker(line, window_length):
    window = []
    for i, c in enumerate(line):
        window.append(c)
        if len(window) > window_length:
            window = window[1:]
        if len(set(window)) == window_length:
            print(f"Start marker {c} found at {i+1}")
            return i
    return 0


if __name__ == "__main__":
    file = "Day06/Day06input.txt"
    read_line(file, lambda l: find_start_marker(l, 4))
    read_line(file, lambda l: find_start_marker(l, 14))
