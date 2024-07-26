// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n

impl Solution {
    pub fn query_string(s: String, n: i32) -> bool {
        for i in 1..=n {
            let binary_str = format!("{:b}", i);
            if !s.contains(&binary_str) {
                return false;
            }
        }
        true
    }
}
