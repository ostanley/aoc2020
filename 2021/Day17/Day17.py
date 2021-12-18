class Trajectory:
    def __init__(self, vx, vy, b):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.bounds = b
        self.height = 0

    def step(self):
        self.x += self.vx
        if self.vx != 0:
            self.vx = self.vx * (1 - 1 / abs(self.vx))

        self.y += self.vy
        self.vy -= 1

        self.height = max(self.height, self.y)
        return self.check_bounds()

    def check_bounds(self):
        if (
            self.bounds["x"][0] <= self.x <= self.bounds["x"][1]
            and self.bounds["y"][0] <= self.y <= self.bounds["y"][1]
        ):
            return 1
        elif self.bounds["x"][1] < self.x or self.bounds["y"][0] > self.y:
            return -1
        else:
            return 0


if __name__ == "__main__":
    bounds = {"x": [277, 318], "y": [-92, -53]}

    # There are some natural bounds vx must be less than the minimum x bound and greater than
    max_height = 0
    count = 0
    for vx in range(1, bounds["x"][1] + 1):
        for vy in range(bounds["y"][0], 1000):
            path = Trajectory(vx, vy, bounds)
            for step in range(10000):
                result = path.step()
                if result < 0:
                    break
                elif result == 1:
                    max_height = max(max_height, path.height)
                    count += 1
                    break
    print(f"Maximum reachable height: {max_height}")
    print(f"Count of correct initial trajectories: {count}")
