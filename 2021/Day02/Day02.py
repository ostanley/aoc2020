from dataclasses import dataclass


@dataclass
class Submarine:
    horiz: int = 0
    depth: int = 0
    aim: int = 0

    def move_sub(self, dir, dist, mode) -> None:
        if dir == "forward":
            self.horiz += dist
            self.depth += dist * self.aim
        elif mode == "p1":
            self.adjust_depth(dir, dist)
        else:
            self.adjust_aim(dir, dist)

    def adjust_aim(self, dir, dist) -> None:
        if dir == "up":
            dist *= -1
        self.aim += dist

    def adjust_depth(self, dir, dist) -> None:
        if dir == "up":
            dist *= -1
        self.depth += dist


if __name__ == "__main__":
    with open("Day02input.txt", "r") as f:
        l = f.readlines()
        sub = Submarine()
        sub2 = Submarine()
        for line in l:
            instructions = line.strip().split(" ")
            sub.move_sub(instructions[0], int(instructions[1]), "p1")
            sub2.move_sub(instructions[0], int(instructions[1]), "p2")

    print(f"Sub 1 is at {sub.horiz, sub.depth} with product {sub.horiz*sub.depth}")

    print(f"Sub 2 is at {sub2.horiz, sub2.depth} with product {sub2.horiz*sub2.depth}")
