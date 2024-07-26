// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn getLength(head: &Option<Box<ListNode>>) -> i32 {
        let mut curr = head;

        let mut n = 0;
        while curr.is_some() {
            curr = &curr.as_ref().unwrap().next as &Option<Box<ListNode>>;
            n += 1;
        }

        return n;
    }

    pub fn getLength_ref(h: Option<Box<ListNode>>) -> i32 {
        let mut curr = h;

        let mut n = 0;
        while curr.is_some() {
            curr = curr.unwrap().next;
            n += 1;
        }

        return n;
    }

    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let mut curr = head;

        let len = Self::getLength(&curr);

        let max_: i32 = (len / 2) as i32 - 1;

        let mut queue = vec![];
        let mut stack = vec![];

        let mut i = 0;

        while i <= max_ {
            let c = curr.unwrap();

            queue.push(c.val);
            
            i += 1;
            curr = c.next;
        }

        while curr.is_some() {
            let c = curr.unwrap();

            stack.push(c.val);
            curr = c.next;
        }

        let len_iter = queue.len();

        let mut ptr = 0;

        let mut max_sum = 0;

        while ptr < len_iter {
            let first = queue[ptr];
            let last = stack[len_iter - ptr - 1];

            if max_sum < (first + last) {
                max_sum = first + last;
            }

            ptr += 1;
        }

        return max_sum
    }
}