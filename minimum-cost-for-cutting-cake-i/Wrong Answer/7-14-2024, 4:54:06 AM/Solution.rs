// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i

impl Solution {
    pub fn minimum_cost(m: i32, n: i32, horizontal_cut: Vec<i32>, vertical_cut: Vec<i32>) -> i32 {
        let mut h_cut = horizontal_cut;
        let mut v_cut = vertical_cut;
        
        h_cut.sort_unstable();
        v_cut.sort_unstable();
        
        let mut h_idx = 0;
        let mut v_idx = 0;
        let mut h_pieces = 1;
        let mut v_pieces = 1;
        let mut total_cost = 0;
        
        while h_idx < h_cut.len() && v_idx < v_cut.len() {
            if h_cut[h_idx] < v_cut[v_idx] {
                total_cost += h_cut[h_idx] * v_pieces;
                h_pieces += 1;
                h_idx += 1;
            } else {
                total_cost += v_cut[v_idx] * h_pieces;
                v_pieces += 1;
                v_idx += 1;
            }
        }
        
        while h_idx < h_cut.len() {
            total_cost += h_cut[h_idx] * v_pieces;
            h_idx += 1;
        }
        
        while v_idx < v_cut.len() {
            total_cost += v_cut[v_idx] * h_pieces;
            v_idx += 1;
        }
        
        total_cost
    }
}
