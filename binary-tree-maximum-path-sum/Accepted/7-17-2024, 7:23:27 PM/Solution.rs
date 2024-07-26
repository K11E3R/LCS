// https://leetcode.com/problems/binary-tree-maximum-path-sum

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_sum = i32::MIN;
        Self::max_path_sum_recursive(&root, &mut max_sum);
        max_sum
    }
    
    fn max_path_sum_recursive(root: &Option<Rc<RefCell<TreeNode>>>, max_sum: &mut i32) -> i32 {
        if let Some(node) = root {
            let node = node.borrow();
            let left_sum = Self::max_path_sum_recursive(&node.left, max_sum).max(0);
            let right_sum = Self::max_path_sum_recursive(&node.right, max_sum).max(0);
            
            let current_path_sum = node.val + left_sum + right_sum;
            *max_sum = (*max_sum).max(current_path_sum);
            
            node.val + left_sum.max(right_sum)
        } else {
            0
        }
    }
}
