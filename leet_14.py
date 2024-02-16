class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       for x in strs[0]:
           print(x)



test1 = ["flower","flow","flight"]
test2 = ["dog","racecar","car"]

Solution().longestCommonPrefix(strs=test1)
Solution().longestCommonPrefix(strs=test2)