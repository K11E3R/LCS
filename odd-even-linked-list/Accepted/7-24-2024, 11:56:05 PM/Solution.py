// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head : return head
        odd, evn, dum = head, head.next, head.next
        while evn and evn.next:
            odd.next, evn.next = odd, evn = odd.next.next, evn.next.next
        odd.next = dum
        return head