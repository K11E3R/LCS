// https://leetcode.com/problems/crawler-log-folder

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut count = 0;
        for log in logs {
            if log == "../" {
                if count > 0 {
                    count -= 1;
                }
            } else if log != "./" {
                count += 1;
            }
        }
        count
    }
}
