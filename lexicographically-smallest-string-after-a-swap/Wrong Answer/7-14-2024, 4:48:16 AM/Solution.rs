// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap

impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();

        for i in 0..n-1 {
            if chars[i].is_digit(10) && chars[i + 1].is_digit(10) {
                let a = chars[i].to_digit(10).unwrap();
                let b = chars[i + 1].to_digit(10).unwrap();
                if (a % 2 == b % 2) && chars[i] > chars[i + 1] {
                    chars.swap(i, i + 1);
                }
            }
        }

        chars.into_iter().collect()
    }
}
