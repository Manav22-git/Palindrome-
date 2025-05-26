class Solution:
    def palindrome (self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

sol = Solution()
print(sol.palindrome(121))