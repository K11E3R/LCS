// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros

impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut ans = Vec::new();
        let mut current = vec![0; n];

        fn dfs(index: usize, current: &mut Vec<u8>, ans: &mut Vec<String>) {
            if index == current.len() {
                ans.push(current.iter().map(|&bit| (bit + b'0') as char).collect());
                return;
            }

            for &bit in &[b'0', b'1'] {
                if index == 0 || current[index - 1] == b'1' {
                    current[index] = bit;
                    dfs(index + 1, current, ans);
                }
            }
        }

        dfs(0, &mut current, &mut ans);

        ans
    }
}