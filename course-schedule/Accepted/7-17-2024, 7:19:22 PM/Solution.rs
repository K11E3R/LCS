// https://leetcode.com/problems/course-schedule

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        // do a topological sort

        let mut indegree = vec![0; num_courses as usize];
        for rule in prerequisites.iter() {
            indegree[rule[1] as usize] += 1;
        }
        
        let mut ready: Vec<_> = indegree
            .iter()
            .enumerate()
            .flat_map(|(i, &indeg)| if indeg == 0 { Some(i) } else { None })
            .collect();
        let mut seen = 0;
        
        while let Some(r) = ready.pop() {
            seen += 1;
            for rule in prerequisites.iter() {
                if rule[0] as usize != r { continue; }
                indegree[rule[1] as usize] -= 1;
                if indegree[rule[1] as usize] == 0 { ready.push(rule[1] as usize); }
            }
        }

        seen == num_courses
    }
}