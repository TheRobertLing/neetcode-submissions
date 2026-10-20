class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        def get_frequencies(s):
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            return tuple(freq)

        for s in strs:
            key = get_frequencies(s)

            anagrams[key].append(s)

        return [item for item in anagrams.values()]
