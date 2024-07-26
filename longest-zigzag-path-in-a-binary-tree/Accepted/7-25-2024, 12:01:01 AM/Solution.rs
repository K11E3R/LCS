// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

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
    pub fn longest_zig_zag(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(n: &Option<Rc<RefCell<TreeNode>>>, l: i32, r: i32) -> i32 {
            match n {
                None => l.max(r),
                Some(n) => {
                    let v = n.borrow();
                    dfs(&v.left, 0, l + 1).max(dfs(&v.right, r + 1, 0))
                }
            }
        }
        dfs(&root, 0, 0) - 1
    }
}