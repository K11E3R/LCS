// https://leetcode.com/problems/max-points-on-a-line

impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut ans = 1;

        for i in 0..n {
            let (x1, y1) = (points[i][0], points[i][1]);
            for j in (i + 1)..n {
                let (x2, y2) = (points[j][0], points[j][1]);
                let mut cnt = 2;
                for k in (j + 1)..n {
                    let (x3, y3) = (points[k][0], points[k][1]);
                    let a = (y2 - y1) * (x3 - x1);
                    let b = (y3 - y1) * (x2 - x1);
                    if a == b {
                        cnt += 1;
                    }
                }
                if cnt > ans {
                    ans = cnt;
                }
            }
        }

        ans
    }
}
