// https://leetcode.com/problems/remove-element

impl Solution{

    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        nums.retain(|&x| x != val);
        nums.len() as i32
    }
/*
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut left = 0;
        for right in 0..nums.len() {
            if nums[right] != val {
                nums[left] = nums[right];
                left += 1;
            }
        }
        left as i32
    }
*/
}