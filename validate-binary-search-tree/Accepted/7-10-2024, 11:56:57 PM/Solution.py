// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root, lbound, rbound):
        if not root:
            return True

        if root.val > lbound and root.val < rbound:
            return self.isValid(root.left, lbound, root.val)\
                and self.isValid(root.right, root.val, rbound)
        
        return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValid(root.left, float('-inf'), root.val)\
            and self.isValid(root.right, root.val, float('inf'))