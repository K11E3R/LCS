// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii

use std::cmp::max;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut f = vec![0; k];
        let mut ans = 0;

        for &num in nums.iter() {
            let x = (num % k as i32) as usize;
            let mut max_lengths = vec![0; k];
            for j in 0..k {
                let y = (j + k - x) % k;
                max_lengths[x] = max(max_lengths[x], f[j] + 1);
            }
            for j in 0..k {
                f[j] = max(f[j], max_lengths[j]);
            }
            ans = max(ans, f[x]);
        }

        ans
    }
}
