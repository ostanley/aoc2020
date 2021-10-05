def memory_game(input, iters):
    number_spoken = 0
    memory = {}
    for i in range(iters):
        if i % 1000000 == 0:
            print(f"Turn {i}")
        if len(input) != 0:
            out_loud = input.pop(0)
            memory[out_loud] = [i]
        elif number_spoken in memory.keys():
            if len(memory[number_spoken]) == 2:
                out_loud = memory[number_spoken][1] - memory[number_spoken][0]
            else:
                out_loud = 0
        else:
            out_loud = 0
        if out_loud in memory.keys():
            memory[out_loud].append(i)
            if len(memory[out_loud]) > 2:
                memory[out_loud].pop(0)
        else:
            memory[out_loud] = [i]

        # print(f'turn {i+1}: Speak {out_loud}')
        # print(memory)
        number_spoken = out_loud

    print(f"Final number spoken {number_spoken}")
    return number_spoken


if __name__ == "__main__":
    starting_string = "12,1,16,3,11,0"
    input = [int(x) for x in starting_string.split(",")]
    iters = 2020
    memory_game(input, iters)
    iters = 30000000
    memory_game(input, iters)
