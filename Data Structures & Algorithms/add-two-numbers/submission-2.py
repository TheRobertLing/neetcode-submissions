# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add in order
        # carry remainder forward

        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 or l2:
            # add the values together
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 1 if total >= 10 else 0
    
            node = ListNode(total if total < 10 else total - 10)

            head.next = node
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            head.next = ListNode(carry)
        
        return dummy.next


