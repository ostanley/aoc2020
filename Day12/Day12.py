import numpy as np


class Ship:
    def __init__(self, position, facing):
        self.position = np.array(position)
        self.facing = np.array(facing)

    def update_position(self, line):
        if line[0] == 'F':
            self.position += int(line[1:])*self.facing
        elif line[0] == 'L' or line[0] == 'R':
            self.turn_ship(line[0], line[1:])
        else:
            self.position = self.move_in_compass_grid(self.position,
                                                      line[0], line[1:])

    def turn_ship(self, dir, rotation_angle):
        rotation = np.array([[0, -1], [1, 0]])
        if dir == 'R':
            rotation = -1*rotation
        turns = int(int(rotation_angle)/90)
        for t in range(turns):
            self.facing = np.dot(self.facing[np.newaxis, :], rotation)
        self.facing = self.facing.flatten()

    def move_in_compass_grid(self, value, dir, distance):
        compass_dict = {'N': np.array([1, 0]),
                        'S': np.array([-1, 0]),
                        'E': np.array([0, 1]),
                        'W': np.array([0, -1])}
        return value + compass_dict[dir]*int(distance)

    def move_to_waypoint(self, waypoint, distance):
        self.position += int(distance)*waypoint.get_relative_position()

    def get_position(self):
        return self.position

    def get_facing(self):
        return self.facing

    def get_manhattan_distance(self):
        return sum([abs(x) for x in self.position])


class Waypoint(Ship):
    def __init__(self, relative_to_ship):
        self.relative_to_ship = np.array(relative_to_ship)

    def update_position(self, line):
        if line[0] == 'L' or line[0] == 'R':
            self.turn_waypoint_around_ship(line[0], line[1:])
        else:
            self.relative_to_ship = self.move_in_compass_grid(
                self.relative_to_ship, line[0], line[1:])

    def turn_waypoint_around_ship(self, dir, rotation_angle):
        rotation = np.array([[0, -1], [1, 0]])
        if dir == 'R':
            rotation = -1*rotation
        turns = int(int(rotation_angle)/90)
        for t in range(turns):
            self.relative_to_ship = np.dot(self.relative_to_ship[np.newaxis, :], rotation)
        self.relative_to_ship = self.relative_to_ship.flatten()

    def get_relative_position(self):
        return self.relative_to_ship


def part1(file):
    ship = Ship([0, 0], [0, 1])
    with open(file, 'r') as f:
        for l in f.readlines():
            ship.update_position(l.strip())

    print(f'Final ship position is {ship.get_position()}',
          f'with Manhattan Distance {ship.get_manhattan_distance()}')


def part2(file):
    ship = Ship([0, 0], [0, 1])
    waypoint = Waypoint([1, 10])
    with open(file, 'r') as f:
        for l in f.readlines():
            if l[0] == 'F':
                ship.move_to_waypoint(waypoint, l.strip()[1:])
            else:
                waypoint.update_position(l.strip())

    print(f'Final ship position is {ship.get_position()}',
          f'with Manhattan Distance {ship.get_manhattan_distance()}')


if __name__ == '__main__':
    file = 'Day12input.txt'

    part1(file)
    part2(file)
