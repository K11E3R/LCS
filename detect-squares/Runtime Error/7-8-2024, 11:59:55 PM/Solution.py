// https://leetcode.com/problems/detect-squares

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_counts = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_counts[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        
        for x2, count2 in self.point_counts.items():
            if x2 != x1:
                d = x2 - x1
                if y1 in count2:
                    count_y1 = self.point_counts[x1][y1]
                    count_y1_plus_d = self.point_counts[x1][y1 + d]
                    count_y1_minus_d = self.point_counts[x1][y1 - d]
                    ans += count2[y1] * count_y1_plus_d * count2[y1 + d]
                    ans += count2[y1] * count_y1_minus_d * count2[y1 - d]
        
        return ans
