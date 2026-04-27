class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) == 1: return s
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j]) and len(longest) < len(s[i:j]):
                    longest = s[i:j]
        return longest
    
    def isPalindrome(self, s:str) -> bool:
        l = 0
        r = len(s) -1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

s = "bb"
a = Solution().longestPalindrome(s)
print(a)