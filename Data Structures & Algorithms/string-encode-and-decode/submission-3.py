class Solution:

    DELIMITER = '-'

    def encode(self, strs: List[str]) -> str:
        """
        encode with the length of the str and a separator indicating where the word starts
        """
        res = ""

        for s in strs:
            res += f"{len(s)}{self.DELIMITER}{s}"

        return res


    def decode(self, s: str) -> List[str]:
        """
        read until the hyphen
        determine the length k
        skip forward k indexes

        """

        strs = []

        idx = 0
        prefix = ''

        while idx < len(s):

            if s[idx] != self.DELIMITER:
                prefix += s[idx]
            else:
                length = int(prefix)
                strs.append(s[idx + 1:idx + 1 + length])
                idx += length
                prefix = ''

            idx += 1

        return strs
