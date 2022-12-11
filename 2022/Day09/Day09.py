import copy
from core.reader import read_line
from enum import Enum


DIRECTION = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [1, 0],
    "D": [-1, 0],
}


class Rope:
    def __init__(self, id, next_rope, head, tail) -> None:
        self.id = id
        self.next_rope = next_rope
        self.head = head
        self.tail = tuple(tail)
        self.tail_history = set([self.tail])

    def update_head_position(self, dir, rope_dict):
        d, dist = dir.split(" ")
        for _ in range(int(dist)):
            self.head = [x + y for x, y in zip(self.head, DIRECTION[d])]
            for i in range(len(rope_dict.keys())):
                if i > 0:
                    rope_dict[i].head = rope_dict[i - 1].tail
                rope_dict[i].update_tail_position(rope_dict)
        return 0

    def update_tail_position(self, rope_dict):
        dist = [int(abs(x - y)) for x, y in zip(self.head, self.tail)]
        if dist[0] < 2 and dist[1] < 2:
            return False
        self.tail = tuple(
            (x - y) / max(abs(x - y), 1) + y for x, y in zip(self.head, self.tail)
        )
        if self.tail not in self.tail_history:
            self.tail_history.update([self.tail])

    def move_rope(self, dir, rope_dict):
        return self.update_head_position(dir, rope_dict)


def print_tail_pic(size, tail_path=set(), head=None, tail=None, rope_dict=None):
    for i in reversed(range(-size[0] // 2, size[0] // 2)):
        for j in range(-size[1] // 2, size[1] // 2):
            print(".", end="")

            if rope_dict is not None:
                for id, rope in rope_dict.items():
                    if (i, j) == rope.tail:
                        print(f"\b{id}", end="")
                    if id == 0 and (i, j) == rope.head:
                        print(f"\bH", end="")
            else:
                if (i, j) in tail_path:
                    print(f"\b#", end="")
                if (i, j) == head:
                    print("\bH", end="")
                if (i, j) == tail:
                    print("\bT", end="")
            if (i, j) == (0, 0):
                print("\bs", end="")
        print("\n", end="")


if __name__ == "__main__":
    file = "Day09/Day09input.txt"
    rope = Rope(0, None, [0, 0], [0, 0])
    read_line(file, lambda x: rope.move_rope(x, {0: rope}))
    print_tail_pic(tail_path=rope.tail_history, size=[10, 10])
    print(f"Tail of rope moved over {len(rope.tail_history)} locations")

    rope_dict = {}
    for i in range(9):  # only 9 knots after head
        rope_dict[i] = Rope(i, i + 1, [0, 0], [0, 0])
    rope_dict[8].next_rope = None
    read_line(file, lambda x: rope_dict[0].move_rope(x, rope_dict))
    print_tail_pic(tail_path=rope_dict[8].tail_history, size=[50, 50])
    print(f"Tail of rope moved over {len(rope_dict[8].tail_history)} locations")
