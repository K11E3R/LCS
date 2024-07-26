// https://leetcode.com/problems/detect-squares

class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.cnt[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for x2 in list(self.cnt.keys()):
            if x2 != x1:
                d = x2 - x1
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 + d] * self.cnt[x2][y1 + d]
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 - d] * self.cnt[x2][y1 - d]
        return ans
