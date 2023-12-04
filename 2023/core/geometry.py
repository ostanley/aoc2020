class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def yield_neighbours(self, diag=True):
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if diag:
            neighbours += [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        for dx, dy in neighbours:
            yield (self.x + dx, self.y + dy)
