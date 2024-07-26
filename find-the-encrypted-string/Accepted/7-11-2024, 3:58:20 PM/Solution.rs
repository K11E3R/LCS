// https://leetcode.com/problems/find-the-encrypted-string


impl Solution {
    pub fn get_encrypted_string(s: String, k: i32) -> String {
        let n = s.len();
        let k = (k as usize) % n;  
        let mut cs = vec![' '; n];
        let s_chars: Vec<char> = s.chars().collect();

        for i in 0..n {
            cs[i] = s_chars[(i + k) % n];
        }

        cs.into_iter().collect()
    }
}
