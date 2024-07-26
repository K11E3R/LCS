// https://leetcode.com/problems/count-good-nodes-in-binary-tree

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0
        }
        let mut stk = vec![(root.unwrap(), -10001i32)];
        let mut cnt = 0i32;

        while let Some((node, val)) = stk.pop() {
            let mut br_node = node.borrow_mut();
            if br_node.val >= val {
                cnt += 1;
            }
            if let Some(tmp_node) = br_node.left.take() {
                stk.push((tmp_node, br_node.val.max(val)));
            }
            if let Some(tmp_node) = br_node.right.take() {
                stk.push((tmp_node, br_node.val.max(val)));
            }
        }

        cnt        
    }
}