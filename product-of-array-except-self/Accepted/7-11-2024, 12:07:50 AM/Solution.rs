// https://leetcode.com/problems/product-of-array-except-self

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut prefix: i32 = 1;
        let mut suffix: i32 = 1;

        let len = nums.len();
        let mut answer = vec![1; len];

        //   wiii
        for index in 0..len {
            let left = index;
            let right = (len - 1) - index;

            answer[left] *= prefix;
            answer[right] *= suffix;

            prefix *= nums[left];
            suffix *= nums[right];
        }

        answer
    }

}