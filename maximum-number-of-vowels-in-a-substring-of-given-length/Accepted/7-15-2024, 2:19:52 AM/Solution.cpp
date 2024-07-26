// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution {
public:
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int cnt = count_if(s.begin(), s.begin() + k, isVowel);
        int ans = cnt;
        for (int i = k; i < s.size(); ++i) {
            cnt += isVowel(s[i]) - isVowel(s[i - k]);
            ans = max(ans, cnt);
        }
        return ans;
    }
};