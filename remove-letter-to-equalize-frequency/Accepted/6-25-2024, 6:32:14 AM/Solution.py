// https://leetcode.com/problems/remove-letter-to-equalize-frequency


class Solution(object):
    def equalFrequency(self, word):
        from collections import Counter
        
        freq_counter = Counter(list(Counter(word).values()))
        
        if len(freq_counter) == 1:
            return len(list(Counter(word).values())) == 1 or 1 in list(Counter(word).values())
        
        if len(freq_counter) == 2:
            (freq1, count1), (freq2, count2) = freq_counter.items()
            if freq1 > freq2:
                freq1, freq2 = freq2, freq1
                count1, count2 = count2, count1
            return (freq1 == 1 and count1 == 1) or (freq2 == freq1 + 1 and count2 == 1)
        
        return False

# class Solution(object):
#     def equalFrequency(self, word):
#         return 'true' if len(word) == len(set(word))+1 else 'false'
