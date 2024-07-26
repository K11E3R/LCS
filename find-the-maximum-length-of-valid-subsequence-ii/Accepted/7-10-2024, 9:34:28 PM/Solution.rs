// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii

use std::cmp::max;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut f = vec![vec![0; k]; k];
        let mut ans = 0;

        for &num in nums.iter() {
            let x = (num % k as i32) as usize;
            for j in 0..k {
                let y = (j + k - x) % k;
                f[x][y] = f[y][x] + 1;
                ans = max(ans, f[x][y]);
            }
        }

        ans
    }
}
