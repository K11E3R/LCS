// https://leetcode.com/problems/build-a-matrix-with-conditions


impl Solution {
    pub fn build_matrix(k: i32, row_conditions: Vec<Vec<i32>>, col_conditions: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        fn topological_sort(k: i32, conditions: Vec<Vec<i32>>) -> Option<Vec<i32>> {
            let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
            let mut indegree = vec![0; (k + 1) as usize];
            
            for condition in conditions {
                let a = condition[0];
                let b = condition[1];
                graph.entry(a).or_insert(vec![]).push(b);
                indegree[b as usize] += 1;
            }

            let mut queue = VecDeque::new();
            for i in 1..=k {
                if indegree[i as usize] == 0 {
                    queue.push_back(i);
                }
            }

            let mut result = vec![];
            while let Some(node) = queue.pop_front() {
                result.push(node);
                if let Some(neighbors) = graph.get(&node) {
                    for &neighbor in neighbors {
                        indegree[neighbor as usize] -= 1;
                        if indegree[neighbor as usize] == 0 {
                            queue.push_back(neighbor);
                        }
                    }
                }
            }

            if result.len() == k as usize {
                Some(result)
            } else {
                None
            }
        }

        let row = topological_sort(k, row_conditions);
        let col = topological_sort(k, col_conditions);
        
        if row.is_none() || col.is_none() {
            return vec![];
        }

        let row = row.unwrap();
        let col = col.unwrap();
        
        let mut ans = vec![vec![0; k as usize]; k as usize];
        let mut col_position = vec![0; (k + 1) as usize];
        
        for (i, &v) in col.iter().enumerate() {
            col_position[v as usize] = i;
        }
        
        for (i, &v) in row.iter().enumerate() {
            ans[i][col_position[v as usize]] = v;
        }

        ans
    }
}
