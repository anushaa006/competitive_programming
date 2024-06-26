class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        a = s[0]
        b = s[1]
        c = s[2]
        count = int(a != b and b !=c and c != a)

        for i in range(3, len(s)):
            a = b
            b = c
            c = s[i]
            count += int(a != b and b !=c and c != a)

        return count