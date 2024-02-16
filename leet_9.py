
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False;
        y = x
        y = str(y)
        y = y[::-1]
        return x == int(y)

print(Solution().isPalindrome(121))