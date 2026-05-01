# https://www.youtube.com/watch?v=XYQecbcd6_c&t=278s
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0

        for i in range(len(s)):
            l = i
            r = i
            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # is palindrome
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return result
s = "babad"
a = Solution().longestPalindrome(s)
print(a)