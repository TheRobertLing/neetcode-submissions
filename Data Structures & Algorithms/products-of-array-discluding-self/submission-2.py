class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        length = len(nums)

        forward = [1] * length
        backward = [1] * length
        res = []

        for i in range(1, length):
            forward[i] = forward[i - 1] * nums[i - 1]
        
        for i in range(length - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]

        for i in range(length):
            res.append(forward[i] * backward[i])
        
        return res