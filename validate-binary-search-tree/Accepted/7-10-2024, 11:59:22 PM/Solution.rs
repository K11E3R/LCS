// https://leetcode.com/problems/validate-binary-search-tree

use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }

// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }


impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, values: &mut Vec<i32>) {
            if let Some(n) = node {
                inorder(&n.borrow().left, values);
                values.push(n.borrow().val);
                inorder(&n.borrow().right, values);
            }
        }
        
        let mut values = Vec::new();
        inorder(&root, &mut values);
        
        for i in 1..values.len() {
            if values[i] <= values[i - 1] {
                return false;
            }
        }
        
        true
    }
}