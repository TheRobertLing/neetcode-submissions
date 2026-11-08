class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # scan over the substring s[i:j]

        # however, this would repeat a lot of work
        # if a letter ever repeats, increasing j would not be helpful since the repeated letter is still there
        # increasing i until the repeated letter is removed is good because
        # imagine if j was fixed and repeated some letter
        # the longest subsequence cannot be some index [i+1,j) regardless of where the repeated letter is
        # because s[i:j-1] would still be at least as long as it

        if len(s) == 0:
            return 0

        longest = 0
        seen = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1



        return max(longest, r - l)


