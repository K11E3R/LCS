// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let n = s.len();
        let mut d = vec![0; n];
        let mut stk = Vec::new();
        let s_chars: Vec<char> = s.chars().collect();

        for (i, &c) in s_chars.iter().enumerate() {
            if c == '(' {
                stk.push(i);
            } else if c == ')' {
                let j = stk.pop().unwrap();
                d[i] = j;
                d[j] = i;
            }
        }

        let mut i = 0;
        let mut x = 1;
        let mut ans = Vec::new();

        while i < n {
            if s_chars[i] == '(' || s_chars[i] == ')' {
                i = d[i];
                x = -x;
            } else {
                ans.push(s_chars[i]);
            }
            i = (i as isize + x) as usize;
        }

        ans.into_iter().collect()
    }
}