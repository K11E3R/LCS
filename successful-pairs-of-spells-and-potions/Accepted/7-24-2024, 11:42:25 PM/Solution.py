// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n=len(potions)
        potions.sort()
        for i in range(len(spells)):
            spells[i]=n-bisect.bisect_left(potions,math.ceil(success/spells[i]))
        return spells