class Submarine:
    def __init__(self) -> None:
        self.horiz = 0
        self.depth = 0
        self.aim = 0

    def move_sub_p1(self, instruction) -> None:
        if instruction[0] == "forward":
            self.horiz += int(instruction[1])
        elif instruction[0] == "up":
            self.depth -= int(instruction[1])
        if instruction[0] == "down":
            self.depth += int(instruction[1])

    def move_sub_p2(self, instruction) -> None:
        if instruction[0] == "forward":
            self.horiz += int(instruction[1])
            self.depth += int(instruction[1]) * self.aim
        elif instruction[0] == "up":
            self.aim -= int(instruction[1])
        if instruction[0] == "down":
            self.aim += int(instruction[1])


if __name__ == "__main__":
    with open("Day02input.txt", "r") as f:
        l = f.readlines()
        sub = Submarine()
        sub2 = Submarine()
        for line in l:
            sub.move_sub_p1(line.strip().split(" "))
            sub2.move_sub_p2(line.strip().split(" "))

    print(f"Sub 1 is at {sub.horiz, sub.depth} with product {sub.horiz*sub.depth}")

    print(f"Sub 2 is at {sub2.horiz, sub2.depth} with product {sub2.horiz*sub2.depth}")
