// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros

impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut ans = Vec::new();
        let mut t = Vec::with_capacity(n); 

        fn dfs(i: usize, n: usize, t: &mut Vec<char>, ans: &mut Vec<String>) {
            if i >= n {
                ans.push(t.iter().collect()); 
                return;
            }
            
            for &j in &[0, 1] {
                if (j == 0 && (i == 0 || t[i - 1] == '1')) || j == 1 {
                    t.push((j + '0' as usize) as u8 as char);
                    dfs(i + 1, n, t, ans);
                    t.pop();
                }
            }
        }

        dfs(0, n, &mut t, &mut ans);

        ans
    }
}