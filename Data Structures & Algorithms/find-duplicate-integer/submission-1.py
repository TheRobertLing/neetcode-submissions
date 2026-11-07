class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # idea tortoise and hare
        # Item in each index represents a node with a pointer.

        # represents the index
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow