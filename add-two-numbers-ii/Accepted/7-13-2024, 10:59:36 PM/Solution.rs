// https://leetcode.com/problems/add-two-numbers-ii

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
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut stack1 = vec![];
        let mut stack2 = vec![];

        let mut p1 = &l1;
        while let Some(node) = p1 {
            stack1.push(node.val);
            p1 = &node.next;
        }

        let mut p2 = &l2;
        while let Some(node) = p2 {
            stack2.push(node.val);
            p2 = &node.next;
        }

        let mut carry = 0;
        let mut result = None;

        while !stack1.is_empty() || !stack2.is_empty() || carry > 0 {
            let mut sum = carry;
            if let Some(digit) = stack1.pop() {
                sum += digit;
            }
            if let Some(digit) = stack2.pop() {
                sum += digit;
            }

            carry = sum / 10;
            let digit = sum % 10;

            // Wiiii make result
            let mut new_node = ListNode::new(digit);
            new_node.next = result;
            result = Some(Box::new(new_node));
        }

        result
    }
}