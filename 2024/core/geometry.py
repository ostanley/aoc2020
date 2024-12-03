class Point2D:
    def __init__(
        self,
        x,
        y,
        value=None,
        neighbours=None,
        default_neighbours=False,
        diag=True,
    ):
        self.x = x
        self.y = y
        if value:
            self.value = value
        if default_neighbours:
            self.neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            if diag:
                self.neighbours += [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        else:
            self.neighbours = neighbours

    def __add__(self, point):
        return Point2D(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point2D(self.x - point.x, self.y - point.y)

    def pos(self):
        return (self.x, self.y)

    def yield_neighbours(self):
        for dx, dy in self.neighbours:
            yield (self.x + dx, self.y + dy)

    def is_connected(self, point):
        n_self = set([p for p in self.yield_neighbours()])
        n_point = set([p for p in point.yield_neighbours()])
        if self.pos() in n_point and point.pos() in n_self:
            return True
        else:
            return False
