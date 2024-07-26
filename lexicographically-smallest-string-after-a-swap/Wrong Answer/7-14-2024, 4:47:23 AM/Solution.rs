// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap

impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        chars.sort_unstable();
        chars.into_iter().collect()
    }
}
