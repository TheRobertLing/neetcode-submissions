# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def set_fast(node, n):
            for i in range(n-1):
                node = node.next

            return node


        dummy = ListNode(0, head)
        prev = dummy
        slow = head
        fast = set_fast(head, n)

        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next

        # slow is on the node to remove
        prev.next = slow.next
        return dummy.next