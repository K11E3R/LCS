// https://leetcode.com/problems/average-waiting-time

impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut spent_time = 0;
        let mut t = 0;
        for customer in &customers {
            let a = customer[0];
            let b = customer[1];
            t = t.max(a) + b;
            spent_time += t - a;
        }
        spent_time as f64 / (customers.len() as f64)
    }
}