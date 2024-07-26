// https://leetcode.com/problems/course-schedule-ii

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let num_courses = num_courses as usize;
        let mut in_degree = vec![0; num_courses];
        let mut graph = vec![vec![]; num_courses];

        for pair in prerequisites {
            let course = pair[0] as usize;
            let prereq = pair[1] as usize;
            graph[prereq].push(course);
            in_degree[course] += 1;
        }

        let mut queue = std::collections::VecDeque::new();
        for i in 0..num_courses {
            if in_degree[i] == 0 {
                queue.push_back(i);
            }
        }

        let mut order = Vec::new();
        while let Some(node) = queue.pop_front() {
            order.push(node as i32);
            for &neighbor in &graph[node] {
                in_degree[neighbor] -= 1;
                if in_degree[neighbor] == 0 {
                    queue.push_back(neighbor);
                }
            }
        }

        if order.len() == num_courses {
            order
        } else {
            Vec::new()
        }
    }
}
