// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut mi = prices[0];
        for &v in &prices {
            ans = ans.max(v - mi);
            mi = mi.min(v);
        }
        ans
    }
}