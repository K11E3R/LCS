// https://leetcode.com/problems/remove-letter-to-equalize-frequency

from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        freq = list(Counter(word).values())
        for i in range(len(freq)):
            if freq[i] == 1 and len(set(freq[:i] + freq[i+1:])) == 1:
                return True
            if freq[i] > 1 and len(set(freq[:i] + [freq[i]-1] + freq[i+1:])) == 1:
                return True
        return False


# class Solution(object):
#     def equalFrequency(self, word):
#         return 'true' if len(word) == len(set(word))+1 else 'false'
