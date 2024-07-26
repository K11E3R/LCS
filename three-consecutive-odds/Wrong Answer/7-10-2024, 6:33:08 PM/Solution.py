// https://leetcode.com/problems/three-consecutive-odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr)-3):
            if  arr[i]%2 and arr[i+1]%2 and arr[i+2]%2:
                return True

        return False  
            
        