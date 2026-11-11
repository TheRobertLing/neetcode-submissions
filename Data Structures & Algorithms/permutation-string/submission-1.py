class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1

        freq2 = {}
        for c in s2[:len(s1)]:
            freq2[c] = freq2.get(c, 0) + 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            if freq1 == freq2:
                return True

            r += 1
            if r < len(s2):
                freq2[s2[r]] = freq2.get(s2[r], 0) + 1

            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]
            l += 1

        return False