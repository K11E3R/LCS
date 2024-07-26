// https://leetcode.com/problems/integer-to-roman

impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let values: Vec<i32> = vec![1000, 900, 500, 400, 100, 90, 50, 40, 10,   9, 5, 4, 1];
        let symbols: Vec<&str> = vec!["M", "CM", "D", "CD", "C", "XC", "L",     "XL", "X", "IX", "V", "IV", "I"];

        let mut result: Vec<&str> = vec![];

        for i in 0..values.len() {
            while num >= values[i] {
                num -= values[i];
                result.push(symbols[i]);
            }
        }
        result.join("")        
    }
}