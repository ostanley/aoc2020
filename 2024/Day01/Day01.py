from collections import Counter

if __name__=="__main__":
    data_file  = "Day01input.txt"

    left_col, right_col = [], []
    with open(data_file, 'r') as f:
        for line in f:
            l, r = [int(x) for x in line.strip().split('   ')]
            left_col.append(l)
            right_col.append(r)

    left_col.sort()
    right_col.sort()

    print("Part 1: {}".format(sum([abs(l-r) for l,r in zip(left_col, right_col)])))

    right_count = Counter(right_col)

    print("Part 2: {}".format(sum([l*right_count[l] for l in left_col])))