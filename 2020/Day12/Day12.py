import numpy as np


def turn_bearing(bearing, dir, rotation_angle):
    rotation = np.array([[0, -1], [1, 0]])
    if dir == 'R':
        rotation = -1*rotation
    turns = int(int(rotation_angle)/90)
    for t in range(turns):
        bearing = np.dot(bearing[np.newaxis, :], rotation)
    return bearing.flatten()


def move_in_compass_grid(position, dir, distance):
    compass_dict = {'N': np.array([1, 0]),
                    'S': np.array([-1, 0]),
                    'E': np.array([0, 1]),
                    'W': np.array([0, -1])}
    return position + compass_dict[dir]*int(distance)


class Ship:
    def __init__(self, position, facing):
        self.position = np.array(position)
        self.facing = np.array(facing)

    def update_position(self, line):
        if line[0] == 'F':
            self.position += int(line[1:])*self.facing
        elif line[0] == 'L' or line[0] == 'R':
            self.facing = turn_bearing(self.facing, line[0], line[1:])
        else:
            self.position = move_in_compass_grid(self.position,
                                                      line[0], line[1:])

    def move_to_waypoint(self, waypoint, distance):
        self.position += int(distance)*waypoint.get_relative_position()

    def get_position(self):
        return self.position

    def get_facing(self):
        return self.facing

    def get_manhattan_distance(self):
        return sum([abs(x) for x in self.position])


class Waypoint():
    def __init__(self, relative_to_ship):
        self.relative_to_ship = np.array(relative_to_ship)

    def update_position(self, line):
        if line[0] == 'L' or line[0] == 'R':
            self.relative_to_ship = turn_bearing(self.relative_to_ship,
                                                              line[0], line[1:])
        else:
            self.relative_to_ship = move_in_compass_grid(
                self.relative_to_ship, line[0], line[1:])

    def get_relative_position(self):
        return self.relative_to_ship


def part1(file):
    ship = Ship([0, 0], [0, 1])
    with open(file, 'r') as f:
        for l in f.readlines():
            ship.update_position(l.strip())
            # print(ship.get_position(), ship.get_facing())

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
            # print(waypoint.get_relative_position())

    print(f'Final ship position is {ship.get_position()}',
          f'with Manhattan Distance {ship.get_manhattan_distance()}')


if __name__ == '__main__':
    file = 'Day12input.txt'

    part1(file)
    part2(file)
