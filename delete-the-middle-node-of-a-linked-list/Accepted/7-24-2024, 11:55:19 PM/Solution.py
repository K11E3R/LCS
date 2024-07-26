// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = head
        slow = ListNode()
        
        slow.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head