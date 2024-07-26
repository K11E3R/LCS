// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap

impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        
        for i in 0..n-1 {
            if (chars[i] as u8) % 2 == (chars[i + 1] as u8) % 2 {
                if chars[i] > chars[i + 1] {
                    chars.swap(i, i + 1);
                    break;
                }
            }
        }
        
        chars.into_iter().collect()
    }
}
