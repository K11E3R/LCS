// https://leetcode.com/problems/power-of-two

impl Solution {
    fn is_power_of_two(n: i32) -> bool {
        n > 0 && (n & (n - 1)) == 0
    }

}