// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary, sentence):
        s = sentence.split(' ')
        l=[]
        for i in range(len(s)):
            f = 0
            for j in dictionary:
                if  j in s[i][0:len(j)] :
                    f = 1
                    l.append(j)
            if f==0 :
                l.append(s[i])		
        
        return " ".join(l)
