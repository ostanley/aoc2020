from core.file_reader import yield_line
import numpy as np


def get_seq_history(seq, pos):
    diff = np.diff(seq)
    if sum(abs(diff)) == 0:
        # base case
        return 0
    elif pos == 0:
        return diff[pos] - get_seq_history(diff, pos)
    else:
        return diff[pos] + get_seq_history(diff, pos)


if __name__ == "__main__":
    file = "Day09input.txt"
    history_sum = 0
    backwards_history_sum = 0
    for seq in yield_line(file):
        seq = [int(s) for s in seq.split(" ")]
        history_sum += get_seq_history(seq, -1) + seq[-1]
        backwards_history_sum += seq[0] - get_seq_history(seq, 0)
        # break
    print("Part 1: Eco history count {}".format(history_sum))
    print("Part 2: Backwards eco history count {}".format(backwards_history_sum))
