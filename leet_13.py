class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for text in s:
            txt = dict[text]
            result += int(txt)
        return result
            
sol = Solution().romanToInt("III")
print(sol)
sol2 = Solution().romanToInt("LVIII")
print(sol2)

sol3 = Solution().romanToInt("MCMXCIV")
print(sol3)
