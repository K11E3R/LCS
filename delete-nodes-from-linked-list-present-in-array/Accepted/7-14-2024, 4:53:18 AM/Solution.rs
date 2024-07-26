// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

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
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        use std::collections::HashSet;
        
        let to_delete: HashSet<i32> = nums.into_iter().collect();
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut current = &mut dummy;
        
        while let Some(ref mut node) = current.next {
            if to_delete.contains(&node.val) {
                current.next = node.next.take();
            } else {
                current = current.next.as_mut().unwrap();
            }
        }
        
        dummy.next
    }
}