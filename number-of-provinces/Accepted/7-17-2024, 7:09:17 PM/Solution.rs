// https://leetcode.com/problems/number-of-provinces

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut is_visited = vec![false; n];
        let mut i = 0;
        let mut provinence_count = 0;
        let mut to_visit = Vec::new();

        while i < n {
            if is_visited[i] {
                i += 1;
                continue;
            }

            provinence_count += 1;
            to_visit.push(i);
            while let Some(j) = to_visit.pop() {
                if is_visited[j] { continue; }
                is_visited[j] = true;
                let connected_it = is_connected[j]
                    .iter()
                    .enumerate()
                    .filter_map(|(k, &is_conn)| (is_conn == 1).then_some(k));
                for k in connected_it {
                    to_visit.push(k);
                }
            }
        }

        provinence_count
    }
}