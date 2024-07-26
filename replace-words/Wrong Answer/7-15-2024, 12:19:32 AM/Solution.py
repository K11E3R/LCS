// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        a = sentence.split(" ")
        for i in range(len(sentence.split(" "))):
            for j in dictionary :
                if j in a[i] :
                    a[i] = j

        return " ".join(a)
                    