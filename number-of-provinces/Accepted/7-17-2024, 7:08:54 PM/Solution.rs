// https://leetcode.com/problems/number-of-provinces

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        fn dfs(is_connected: &Vec<Vec<i32>>, visited: &mut Vec<bool>, i: usize) {
            for j in 0..is_connected.len() {
                if is_connected[i][j] == 1 && !visited[j] {
                    visited[j] = true;
                    dfs(is_connected, visited, j);
                }
            }
        }

        let n = is_connected.len();
        let mut visited = vec![false; n];
        let mut count = 0;

        for i in 0..n {
            if !visited[i] {
                dfs(&is_connected, &mut visited, i);
                count += 1;
            }
        }

        count
    }
}