// https://leetcode.com/problems/average-waiting-time

impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut tot = 0;
        let mut t = 0;
        for customer in &customers {
            let a = customer[0];
            let b = customer[1];
            t = t.max(a) + b;
            tot += t - a;
        }
        tot as f64 / (customers.len() as f64)
    }
}