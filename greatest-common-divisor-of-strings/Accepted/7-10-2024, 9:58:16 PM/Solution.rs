// https://leetcode.com/problems/greatest-common-divisor-of-strings

impl Solution {    
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        if str1.len() < str2.len() {
            return Self::gcd_of_strings(str2, str1);
        }
        
        if str1[..str2.len()] == *str2 {
            let remaining = &str1[str2.len()..];
            if remaining.is_empty() {
                return str2
            }
            else {
                return Self::gcd_of_strings(remaining.to_string(), str2)
            }
        }
        "".to_string()
    }
}