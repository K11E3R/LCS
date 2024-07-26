// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")
        def dfs(node):
            nonlocal prev

            if not node:
                return True

            left = dfs(node.left)
            if prev >= node.val:
                result = False
                return
            
            prev = node.val
            right = dfs(node.right)

            return right and left

        return dfs(root)
        # return result