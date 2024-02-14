class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        length = len(s)

        for i in range(length):
            l = r = i

            while r < length and l >= 0 and s[r] == s[l]:
                if r - l + 1 >= resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                r += 1
                l -= 1

            r = i + 1
            l = i

            while r < length and l >= 0 and s[r] == s[l]:
                if r - l + 1 >= resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                r += 1
                l -= 1

        return res
