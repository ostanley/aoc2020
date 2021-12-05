from dataclasses import dataclass
from operator import add, sub

sign = lambda x: (1, -1)[x < 0]


@dataclass
class VentLocation:
    x: int
    y: int

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return VentLocation(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return VentLocation(self.x - other.x, self.y - other.y)

    def to_list(self):
        return [self.x, self.y]


@dataclass
class SeaFloor:
    safe_locations: dict
    dangerous_locations: dict
    id: int = 0

    def add_vent(self, start: VentLocation, end: VentLocation, rules="straight"):
        self.id += 1
        dist = end - start

        if dist.x == 0:
            step_dir = VentLocation(0, sign(dist.y))
        elif dist.y == 0:
            step_dir = VentLocation(sign(dist.x), 0)
        elif rules != "straight":
            step_dir = VentLocation(sign(dist.x), sign(dist.y))
        else:
            return

        pos = start
        while pos != end + step_dir:
            self.add_vent_location(pos)
            pos = pos + step_dir

    def add_vent_location(self, point: VentLocation):
        if point in self.dangerous_locations.keys():
            self.dangerous_locations[point].append(self.id)
        elif point in self.safe_locations.keys():
            vents = self.safe_locations.pop(point)
            vents.append(self.id)
            if len(vents) >= 2:
                self.dangerous_locations[point] = vents
            else:
                self.safe_locations[point] = vents
        else:
            self.safe_locations[point] = [self.id]


if __name__ == "__main__":
    with open("Day05input.txt", "r") as f:
        seafloor_p1 = SeaFloor({}, {})
        seafloor_p2 = SeaFloor({}, {})
        for line in f.readlines():
            points = line.strip().split()
            start = VentLocation(*[int(x) for x in points[0].split(",")])
            end = VentLocation(*[int(x) for x in points[2].split(",")])
            seafloor_p1.add_vent(start, end, "straight")
            seafloor_p2.add_vent(start, end, "full")

    print(
        f"There are {len(seafloor_p1.dangerous_locations)} seafloor straightline vent intersections."
    )
    print(
        f"There are {len(seafloor_p2.dangerous_locations)} seafloor total vent intersections."
    )
