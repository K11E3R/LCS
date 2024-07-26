// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        mi = min(len(w) for w in d)
        ma = max(len(w) for w in d)
        words = sentence.split()
        res = []
        for w in words:
            for i in range(mi, min(ma, len(w)) + 1):
                if w[:i] in d:
                    w = w[:i]
                    break
            res.append(w)

        return ' '.join(res)