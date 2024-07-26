// https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 < stack[-1]:
                if -i > stack[-1]:
                    stack.pop()
                    continue
                elif -i == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack
f = open("user.out", "w")
for case in map(loads, stdin):
    print(str(Solution().asteroidCollision(case)).replace(" ",""), file = f)
f.close()
exit(0)