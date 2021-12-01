from collections import deque

if __name__ == "__main__":
    count_inc = 0
    with open("Day01input.txt", "r") as f:
        depth = f.readline().strip()

        while depth != "":
            depth_new = f.readline().strip()
            if depth_new == "":
                break
            if int(depth) < int(depth_new):
                count_inc += 1
            depth = depth_new
    print(f"The depth increases {count_inc} times")

    deque_size = 3
    count_inc = 0
    with open("Day01input.txt", "r") as f:
        window = deque()
        for r in range(deque_size):
            window.append(f.readline().strip())
        depth_new = f.readline().strip()
        while depth_new != "":
            # print(window, depth_new, sum([int(x) for x in window]))
            if int(window.popleft()) < int(depth_new):
                count_inc += 1
            window.append(depth_new)
            depth_new = f.readline().strip()
    print(f"The sliding window 3 depth increases {count_inc} times")
