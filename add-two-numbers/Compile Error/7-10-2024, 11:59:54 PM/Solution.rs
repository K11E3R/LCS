// https://leetcode.com/problems/add-two-numbers

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
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy_head = ListNode::new(0);
        let (mut p, mut q, mut current) = (&l1, &l2, &mut dummy_head);
        let mut carry = 0;

        while p.is_some() || q.is_some() {
            let sum = carry
                + p.map_or(0, |node| {
                    let val = node.val;
                    p = &node.next;
                    val
                })
                + q.map_or(0, |node| {
                    let val = node.val;
                    q = &node.next;
                    val
                });

            carry = sum / 10;
            current.next = Some(Box::new(ListNode::new(sum % 10)));
            current = current.next.as_mut().unwrap();
        }

        if carry > 0 {
            current.next = Some(Box::new(ListNode::new(carry)));
        }

        dummy_head.next
    }
}