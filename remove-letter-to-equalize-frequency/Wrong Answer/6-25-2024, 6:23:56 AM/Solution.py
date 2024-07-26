// https://leetcode.com/problems/remove-letter-to-equalize-frequency

class Solution(object):
    def equalFrequency(self, word):
        set_len = len(set(word))+1
        return "true" if len(word) == set_len else "false"