if __name__ == "__main__":
    with open("Day06input.txt") as f:
        memory = [int(x) for x in f.readlines()[0].strip().split("\t")]

    # memory = [0, 2, 7, 0]

    seen_memory = {}
    step = 0
    while tuple(memory) not in seen_memory.keys():
        seen_memory[tuple(memory)] = step

        add_memory = max(memory)
        ind_memory = memory.index(add_memory)
        num_memory = round(add_memory / len(memory))

        memory[ind_memory] = 0

        for i in range(1, len(memory) + 1):
            if i * num_memory > add_memory:
                num_memory = add_memory - (i - 1) * num_memory
            if ind_memory + i >= len(memory):
                i -= len(memory)
            memory[ind_memory + i] += num_memory

        step += 1

    print(f"Took {step} steps to reach a loop.")
    print(f"Loop is {step-seen_memory[tuple(memory)]} steps long.")
