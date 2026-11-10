class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keep running counter of which character appears over 1/2 the time
        # after each iteration increase the window and determine count
        # record the longest length
        # The window keeps increasing as long as there are replacements to spare
        # 

        l = 0
        best = 0
        counts = {}

        for r in range(len(s)):
            # expand the substring whilst there is k to spare
            counts[s[r]] = counts.get(s[r], 0) + 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best