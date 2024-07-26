// https://leetcode.com/problems/largest-values-from-labels

use std::collections::HashMap;

impl Solution {
    pub fn largest_vals_from_labels(values: Vec<i32>, labels: Vec<i32>, num_wanted: i32, use_limit: i32) -> i32 {
        let mut items: Vec<(i32, i32)> = values.iter().zip(labels.iter()).map(|(&v, &l)| (v, l)).collect();
        items.sort_by_key(|&(v, _)| -v); // sort desc
        
        let mut selected_count: HashMap<i32, i32> = HashMap::new();
        let mut selected_total = 0;
        let mut num_selected = 0;
        
        for (value, label) in items {
            if num_selected >= num_wanted {
                break;
            }
            
            let count = selected_count.entry(label).or_insert(0);
            if *count < use_limit {
                *count += 1;
                selected_total += value;
                num_selected += 1;
            }
        }
        
        selected_total
    }
}