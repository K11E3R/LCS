// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut res = 0;
        for i in 1..prices.len() {
            res += (0).max(prices[i] - prices[i - 1]);
        }
        res
    }
}