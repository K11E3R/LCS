// https://leetcode.com/problems/search-insert-position

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut low = 0;
        let mut high = nums.len() - 1;

        while low <= high {
            let mid = low + (high - low)/2;
            
            if *nums.get(mid).unwrap() == target {
                return mid as i32;
            } else if *nums.get(mid).unwrap() < target {
                low = mid + 1;
            } else {
                if mid == 0 {
                    // break;
                    return mid as i32;
                }
                high = mid - 1;
            }
        }
        return low as i32;
    }
}