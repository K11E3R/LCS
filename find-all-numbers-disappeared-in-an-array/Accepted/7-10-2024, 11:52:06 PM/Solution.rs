// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        use std::collections::HashSet;
        
        let mut num_set: HashSet<i32> = HashSet::new();
        let mut result: Vec<i32> = Vec::new();
        for &num in nums.iter() {
            num_set.insert(num);
        }
        
        for i in 1..=nums.len() as i32 {
            if !num_set.contains(&i) {
                result.push(i);
            }
        }
        
        result
    }
}
