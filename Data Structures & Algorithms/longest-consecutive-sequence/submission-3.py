class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # how do we find which numbers are starting numbers
        # they are starting numbers if n - 1 doesnt exist

        numbers = set(nums)
        starts = []
        max_len = 0

        for num in nums:
            if num - 1 in numbers:
                continue
            
            starts.append(num)

        for start in starts:
            curr_length = 1

            while start + 1 in numbers:
                curr_length += 1
                start += 1
            
            max_len = max(max_len, curr_length)

        return max_len