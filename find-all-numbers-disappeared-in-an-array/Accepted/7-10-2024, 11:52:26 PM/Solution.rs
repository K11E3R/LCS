// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut result_array = vec![0; nums.len() + 1];
        let mut ans: Vec<i32> = Vec::new();

        for index in 0..nums.len() {
            result_array[nums[index] as usize] = nums[index] as usize;
        }

        for (index, element) in result_array.iter().skip(1).enumerate() {
            if *element == 0 { ans.push((index + 1) as i32) }
        }

        ans
    }
}