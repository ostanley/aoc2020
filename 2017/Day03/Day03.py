import numpy as np

rot_90 = np.array([[0, -1], [1, 0]])

class SpiralCounter:
    def __init__(self, store=False):
        self.pos = [0, 0]
        self.store = store
        if self.store:
            self.pos_dict = {0: {0:1}}
        self.value = 1
        self.steps = 1
        self.ring = 1
        self.cardinal = [-1, 0]

    def rotate90(self):
        self.steps = 0
        self.cardinal = np.dot(self.cardinal, rot_90)

    def movering(self):
        self.step()
        self.rotate90()
        self.steps += 1
        self.ring += 2

    def step(self):
        self.pos = np.add(self.pos, self.cardinal)
        if self.store:
            if self.pos[0] not in self.pos_dict.keys():
                self.pos_dict[self.pos[0]] = {}
            self.pos_dict[self.pos[0]][self.pos[1]]=self.get_neighbour_sum()
        self.value += 1
        self.steps += 1

    def get_neighbour_sum(self):
        offsets = [[0, -1], [1, -1],[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1]]
        sum = 0
        for x in offsets:
            new_pos = np.add(self.pos,x)
            if new_pos[0] in self.pos_dict.keys():
                if new_pos[1] in self.pos_dict[new_pos[0]].keys():
                    sum += self.pos_dict[new_pos[0]][new_pos[1]]
        return sum


def is_odd_square(val):
    if val - np.floor(np.sqrt(val)) ** 2 < 10 ** (-10):
        # is square
        if np.floor(np.sqrt(val)) % 2 != 0:
            return True
    return False


def find_spiral_position(input, store=False):
    spiral = SpiralCounter(store=store)
    while spiral.value < input:
        if is_odd_square(spiral.value):
            spiral.movering()
        if spiral.steps == spiral.ring - 1:
            spiral.rotate90()
        spiral.step()
        if store and spiral.pos_dict[spiral.pos[0]][spiral.pos[1]] > input:
            return spiral.pos_dict[spiral.pos[0]][spiral.pos[1]]
    if store:
            return -1
    return abs(spiral.pos[0]) + abs(spiral.pos[1])


if __name__ == "__main__":
    input = 289326
    print(f"{input} is {find_spiral_position(input)} steps away.")
    print(f"{input} has value {find_spiral_position(input, store=True)}.")
