# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        def split(head):
            prev, slow, fast = None, head, head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            return head, slow


        def reverse(head):
            p1, p2 = None, head
            while p2:
                temp = p2.next
                p2.next = p1
                p1 = p2
                p2 = temp

            return p1

        def merge(list1, list2):
            current = list2
            prev = None
            while list1:
                temp = list1.next
                list1.next = current
                current = current.next

                list1 = list1.next
                list1.next = temp
                prev = list1
                list1 = list1.next

            prev.next = current



        list1, list2 = split(head)
        list2 = reverse(list2)
        merge(list1, list2)