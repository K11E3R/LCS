// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

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
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        // let mut root = root;
        if let Some(node) = root.clone() {
            let node = node.borrow();
            if let (Some(p1), Some(q1)) = (p.clone(), q.clone()) {
                if node.val == p1.borrow().val || node.val == q1.borrow().val {
                    return root;
                }
            }
            
            let left = Self::lowest_common_ancestor(node.left.clone(), p.clone(), q.clone());
            let right = Self::lowest_common_ancestor(node.right.clone(), p.clone(), q.clone());

            if left.is_some() && right.is_some() {
                return root;
            }

            if left.is_some() {
                return left;
            }
            if right.is_some() {
                return right;
            }
        }
        None
    }
}