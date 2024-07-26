// https://leetcode.com/problems/path-sum-iii

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
type Tree = Rc<RefCell<TreeNode>>;
impl Solution {
    pub fn path_sum(root: Option<Tree>, target_sum: i32) -> i32 {
        fn recurse(root: Option<&Tree>, vec: &mut Vec<i64>, target: i64) -> i64 {
            if let Some(node) = root {
                let val = node.borrow().val as i64;
                vec.iter_mut().for_each(|x| *x += val); vec.push(val);
                let max = vec.iter().filter(|&x| x == &target).count() as i64 
                        + recurse(node.borrow().left.as_ref(), vec, target)
                        + recurse(node.borrow().right.as_ref(), vec, target);
                vec.pop(); vec.iter_mut().for_each(|x| *x -= val);
                max
            } else { 0 }
        } 
        recurse(root.as_ref(), &mut vec![], target_sum as i64) as i32
    }
}