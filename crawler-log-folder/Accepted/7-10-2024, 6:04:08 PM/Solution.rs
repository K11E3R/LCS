// https://leetcode.com/problems/crawler-log-folder

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut count = 0;
        for log in logs.iter() {
            match log.as_str() {
                "../" => if count > 0 { count -= 1; },
                "./" => {},
                _ => count += 1,
            }
        }
        count
    }
}
