// https://leetcode.com/problems/cherry-pickup-ii

impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp = vec![vec![i32::MIN; n]; n];
        dp[0][n - 1] = grid[0][0] + grid[0][n - 1];
        
        for i in 1..m {
            let mut new_dp = vec![vec![i32::MIN; n]; n];
            for j1 in 0..n {
                for j2 in 0..n {
                    let val = grid[i][j1] + if j1 == j2 { 0 } else { grid[i][j2] };
                    for y1 in (j1.saturating_sub(1))..=(j1 + 1).min(n - 1) {
                        for y2 in (j2.saturating_sub(1))..=(j2 + 1).min(n - 1) {
                            if dp[y1][y2] != i32::MIN {
                                new_dp[j1][j2] = new_dp[j1][j2].max(dp[y1][y2] + val);
                            }
                        }
                    }
                }
            }
            dp = new_dp;
        }
        
        dp.into_iter().flatten().max().unwrap_or(0)
    }
}
