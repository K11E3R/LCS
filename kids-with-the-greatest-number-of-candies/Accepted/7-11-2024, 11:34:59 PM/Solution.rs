// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let max = *candies.iter().max().unwrap();
        candies.iter().map(|v| v + extra_candies >= max).collect()
    }
}