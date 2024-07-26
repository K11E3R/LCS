// https://leetcode.com/problems/leaf-similar-trees

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
impl Solution {
    pub fn leaf_similar(root1: Option<Box<TreeNode>>, root2: Option<Box<TreeNode>>) -> bool {
        let mut list1 = Vec::new();
        let mut list2 = Vec::new();
        recursion(&root1, &mut list1);
        recursion(&root2, &mut list2);
        list1 == list2
    }

    fn recursion(node: &Option<Box<TreeNode>>, leaf_list: &mut Vec<i32>) {
        if let Some(node) = node {
            if node.left.is_none() && node.right.is_none() {
                leaf_list.push(node.val);
            }
            recursion(&node.left, leaf_list);
            recursion(&node.right, leaf_list);
        }
    }
}