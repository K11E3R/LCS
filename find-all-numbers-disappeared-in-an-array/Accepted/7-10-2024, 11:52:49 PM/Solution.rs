// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

impl Solution {
    pub fn find_disappeared_numbers(mut nums: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::with_capacity(nums.len()+1);
        res.resize(nums.len()+1, 0);
        for &i in &nums {
            res[i as usize] = i;
        }
        
        nums.clear();
        
        for i in 1..res.len() {
            if res[i] == 0 {
                nums.push(i as i32);
            }
        }
        nums
    }
}