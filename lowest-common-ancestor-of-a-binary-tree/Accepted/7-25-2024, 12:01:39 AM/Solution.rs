// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Tree,
//   pub right: Tree,
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

type Tree = Option<Rc<RefCell<TreeNode>>>;

#[repr(u8)]
#[derive(Copy, Clone, PartialEq, Eq)]
enum Direction {Left, Right}

use Direction::*;

fn get_node(tree: Tree, path: Vec<Direction>) -> Tree {
    let mut curr_node = tree;

    if !path.is_empty() {
        for dir in path {
            match dir {
                Left => curr_node = curr_node.map(|n| n.borrow().left.clone()).flatten(),
            
                Right => curr_node = curr_node.map(|n| n.borrow().right.clone()).flatten(),
            }
        }
    }

    curr_node
}

fn get_path_to_node(root: Tree, target: Tree) -> Vec<Direction> {
    let target_node = target.unwrap();
    let root_node = root.unwrap();

    let mut node_stack: Vec<(Rc<RefCell<TreeNode>>, Vec<Direction>)> = vec![(root_node.clone(), vec![])];

    while let Some((node, path)) = node_stack.pop() {
        if node == target_node {
            return path;
        }

        if let Some(ln) = node.borrow().left.as_ref() {
            let mut left_path = path.clone();
            left_path.push(Left);
            node_stack.push((ln.clone(), left_path));
        }

        if let Some(rn) = node.borrow().right.as_ref() {
            let mut right_path = path.clone();
            right_path.push(Right);
            node_stack.push((rn.clone(), right_path));
        }
    }

    vec![]
}


impl Solution {
    pub fn lowest_common_ancestor(root: Tree, p: Tree, q: Tree) -> Tree {
        let p_path = get_path_to_node(root.clone(), p.clone());
        let q_path = get_path_to_node(root.clone(), q.clone());

        let lca_path = p_path.into_iter()
            .zip(q_path.into_iter())
            .take_while(|(p_dir, q_dir)| p_dir == q_dir)
            .map(|tup_dir| tup_dir.0)
            .collect::<Vec<Direction>>();

        get_node(root.clone(), lca_path)
    }
}