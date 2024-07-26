// https://leetcode.com/problems/detect-squares

use std::collections::HashMap;

struct DetectSquares {
    cnt: HashMap<i32, HashMap<i32, i32>>,
}

impl DetectSquares {
    fn new() -> Self {
        Self {
            cnt: HashMap::new(),
        }
    }
    
    fn add(&mut self, point: Vec<i32>) {
        let x = point[0];
        let y = point[1];
        *self.cnt.entry(x).or_insert_with(HashMap::new).entry(y).or_insert(0) += 1;
    }
    
    fn count(&self, point: Vec<i32>) -> i32 {
        let x1 = point[0];
        let y1 = point[1];
        if !self.cnt.contains_key(&x1) {
            return 0;
        }
        let mut ans = 0;
        
        for (&x2, cnt2) in &self.cnt {
            if x2 != x1 {
                let d = x2 - x1;
                if let Some(cnt1) = self.cnt.get(&x1) {
                    if let Some(&cnt_y1_d) = cnt1.get(&(y1 + d)) {
                        if let Some(&cnt_y2_d) = cnt2.get(&(y1 + d)) {
                            ans += cnt2[&y1] * cnt_y1_d * cnt_y2_d;
                        }
                    }
                    if let Some(&cnt_y1_d) = cnt1.get(&(y1 - d)) {
                        if let Some(&cnt_y2_d) = cnt2.get(&(y1 - d)) {
                            ans += cnt2[&y1] * cnt_y1_d * cnt_y2_d;
                        }
                    }
                }
            }
        }
        
        ans
    }
}
