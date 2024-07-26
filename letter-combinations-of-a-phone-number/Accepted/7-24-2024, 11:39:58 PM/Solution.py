// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        answer = []

        if not digits:
            return []
  
        def findCombo(i, subset):
            if len(subset) == len(digits):
                answer.append(subset)
                return
            
            for char in digitToLetter[digits[i]]:
                findCombo(i+1, subset+char)

        findCombo(0, "")
        
        return answer
