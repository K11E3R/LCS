// https://leetcode.com/problems/validate-binary-search-tree

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
use std::collections::VecDeque;
impl Solution {
pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
    let Some(root) = root else {
        return true;
    };
    let mut queue: VecDeque<(Rc<RefCell<TreeNode>>, Option<i32>, Option<i32>)> = VecDeque::new();

    queue.push_back((Rc::clone(&root), None, None));

    while let Some((current_node_rc, lower_bound, upper_bound)) = queue.pop_front() {
        let current_node = current_node_rc.borrow();

        if let Some(lower) = lower_bound {
            if current_node.val <= lower {
                return false;
            }
        }
        if let Some(upper) = upper_bound {
            if current_node.val >= upper {
                return false;
            }
        }

        if let Some(left_rc) = &current_node.left {
            queue.push_back((Rc::clone(left_rc), lower_bound, Some(current_node.val)));
        }
        if let Some(right_rc) = &current_node.right {
            queue.push_back((Rc::clone(right_rc), Some(current_node.val), upper_bound));
        }
    }
    true
}
}