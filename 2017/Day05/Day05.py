if __name__ == "__main__":
    with open("Day05input.txt") as f:
        instructions = [int(x.strip()) for x in f.readlines()]

    # instructions = [0,3,0,1,-3]

    step = 0
    x = 0
    part2 = False
    while x < len(instructions):
        if instructions[x] >= 3 and part2 == True:
            instructions[x] -= 1
            x += instructions[x] + 1
        else:
            instructions[x] += 1
            x += instructions[x] - 1
        step += 1

    print(f"Loop exited in {step} steps.")
