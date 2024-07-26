// https://leetcode.com/problems/product-of-array-except-self


impl Solution {
    pub fn product_except_self(mut nums: Vec<i32>) -> Vec<i32> {
        let zeroes = nums.iter().filter(|&&v| v == 0).count();
        let product: i32 = nums.iter().filter(|&&v| v != 0).product();

        if zeroes == 1 {
            for i in 0..nums.len() {
                if nums[i] == 0 {
                    nums[i] = product;
                } else {
                    nums[i] = 0;
                }
            }
            // Wiiiiii
        } else if zeroes > 1 {
            for i in 0..nums.len() {
                nums[i] = 0;
            }
        } else if zeroes == 0 {
            for i in 0..nums.len() {
                if nums[i] != 0 {
                    nums[i] = product / nums[i];
                }
            }
        }

        nums
    }
}