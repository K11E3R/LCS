// https://leetcode.com/problems/merge-nodes-in-between-zeros

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()  
        current = dummy
        
        sum_non_zero = 0
        
        while head:
            if head.val == 0:
                if sum_non_zero > 0:
                    current.next = ListNode(sum_non_zero)
                    current = current.next
                    sum_non_zero = 0
            else:
                sum_non_zero += head.val
            
            head = head.next
        
        if sum_non_zero > 0:
            current.next = ListNode(sum_non_zero)
        
        return dummy.next
