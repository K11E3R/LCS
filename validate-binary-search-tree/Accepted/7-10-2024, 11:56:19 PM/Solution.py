// https://leetcode.com/problems/validate-binary-search-tree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        values = inorder(root)
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        return True