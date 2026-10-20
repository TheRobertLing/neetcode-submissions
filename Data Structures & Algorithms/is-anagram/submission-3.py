class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # They are an anagram if the frequency of the letters that appears is the same
        return Counter(s) == Counter(t)
