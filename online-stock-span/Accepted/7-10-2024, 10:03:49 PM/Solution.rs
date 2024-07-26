// https://leetcode.com/problems/online-stock-span

/*
use std::collections::VecDeque;

struct StockSpanner {
    stk: VecDeque<(i32, i32)>,
}

impl StockSpanner {
    fn new() -> Self {
        Self {
            stk: VecDeque::new(),
        }
    }

    fn next(&mut self, price: i32) -> i32 {
        let mut cnt = 1;
        
        while let Some(&(p, s)) = self.stk.back() {
            if p <= price {
                cnt += s;
                self.stk.pop_back();
            } else {
                break;
            }
        }
        
        self.stk.push_back((price, cnt));
        cnt
    }
}

*/

struct StockSpanner {
    prices: Vec<(usize,i32)>
}

impl StockSpanner {

    fn new() -> Self {
        StockSpanner{
            prices: Vec::<(usize,i32)>::new(),
        }
    }
    
    fn next(&mut self, price: i32) -> i32 {
        let mut span = 1;
        while let Some((p_span, pp)) = self.prices.last() {
            if *pp > price {
                break;
            }
            span += p_span;
            self.prices.pop();
        }
        self.prices.push((span, price));
        span as i32
    }
}