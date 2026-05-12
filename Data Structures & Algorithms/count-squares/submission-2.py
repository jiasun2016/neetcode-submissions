class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.ptsCount):
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, y)]*self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res