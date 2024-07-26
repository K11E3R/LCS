// https://leetcode.com/problems/number-of-provinces

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut visited = vec![false; n];
        let mut count = 0;

        for i in 0..n {
            if !visited[i] {
                count += 1;
                let mut stack = vec![i];
                
                while let Some(node) = stack.pop() {
                    for j in 0..n {
                        if is_connected[node][j] == 1 && !visited[j] {
                            visited[j] = true;
                            stack.push(j);
                        }
                    }
                }
            }
        }

        count
    }
}
