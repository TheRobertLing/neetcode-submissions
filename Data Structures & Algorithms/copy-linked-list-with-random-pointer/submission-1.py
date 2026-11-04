"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return

        clones_map = {}
        clones = []

        # create clones
        curr = head
        while curr:
            clone = Node(curr.val)
            clones.append(clone)

            # maps each original value to it's own clone
            clones_map[curr] = clone
            curr = curr.next

        # attach node.next
        for index, clone in enumerate(clones):
            if index == len(clones) - 1:
                clone.next = None
            else:
                clone.next = clones[index+1]

        # attach node.random
        curr = head
        while curr:
            clone = clones_map[curr]
            random_clone = clones_map[curr.random] if curr.random else None
            clone.random = random_clone
            curr = curr.next

        return clones[0]




