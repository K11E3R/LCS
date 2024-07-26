// https://leetcode.com/problems/product-of-array-except-self

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let total_product = nums.iter().product::<i32>();
        let n = nums.len();
        nums.into_iter().map(|num| total_product / num).collect::<Vec<i32>>()
    }
}