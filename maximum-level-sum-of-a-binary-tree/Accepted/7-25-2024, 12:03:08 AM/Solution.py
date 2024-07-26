// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        deq=deque([root])
        if not root:
            return 0 
        ma=[float('-inf'),0]
        i=0
        while deq:
            i+=1
            new_deque=deque([])
            su=0
            while deq:
                node=deq.popleft()
                su+=node.val
                if node.left:
                    new_deque.append(node.left)
                if node.right:
                    new_deque.append(node.right)
            deq=new_deque.copy()
            if ma[0]<su:
                ma=[su,i]
        return ma[1]

            


                


            
                


            