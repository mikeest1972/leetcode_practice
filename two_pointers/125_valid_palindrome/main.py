# 

class Solution:
    # time complexity O(n)
    def isPalindrome(self, s: str) -> bool:
        # base case
        if s == "": return True
        # remove non alpha numeric char and make them lowercase
        s = ''.join(filter(str.isalnum, s)).lower()

        l = 0
        r = len(s) -1
        while l < r:
            if s[l] == s[r]:
                # move the pointers
                l += 1
                r -= 1
            else:
                return False
        return True

s = "race a car"
a = Solution().isPalindrome(s)
print(a)
