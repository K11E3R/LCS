// https://leetcode.com/problems/water-bottles

impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let (mut empty_bottles, mut total_bottles) = (num_bottles, num_bottles);

        while empty_bottles >= num_exchange {
            let new_bottles = empty_bottles / num_exchange;
            total_bottles += new_bottles;
            empty_bottles = empty_bottles % num_exchange + new_bottles;
        }

        total_bottles
    }
}
