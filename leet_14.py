

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            res = ""
            strs.sort()
            maxLen = min(len(strs[0]), len(strs[-1]))
            for i in range(maxLen):
                if strs[0][i] is not strs[-1][i]:
                     return res
                res += strs[0][i]
            return res

test1 = ["flower","flow","flight"]
test2 = ["dog","racecar","car"]
test3 = ["ab", "a"]

res1 = Solution().longestCommonPrefix(strs=test1)
res2 = Solution().longestCommonPrefix(strs=test2)
res3 = Solution().longestCommonPrefix(strs=test3)
print(res1)
print(res2)
print(res3)
