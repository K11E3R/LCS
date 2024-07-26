// https://leetcode.com/problems/product-of-array-except-self

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let zero_count = nums.iter().filter(|&x| *x == 0).count();

        if zero_count > 1 {
            return vec![0; nums.len()];
        }

        let total_product = nums.iter().filter(|&x| *x != 0).product::<i32>();
        nums.into_iter().map(|num| {
            if num == 0 {
                total_product
            } else if zero_count == 1 {
                0
            } else {
                total_product / num
            }
        }).collect::<Vec<i32>>()
    }

}