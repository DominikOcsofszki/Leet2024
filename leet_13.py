class Solution:
    def rules(self, a, b):
        if(a == 1 and (b == 5 or b == 10)):
            return b - a, True
        if(a == 10 and (b == 50 or b == 100)):
            return b - a, True
        if(a == 100 and (b == 500 or b == 1000)):
            return b - a, True
        return a, False
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
        skip = False
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            nr = int(dict[s[i]])
            if i == len(s) - 1:
                result += nr
                continue
            nr_next = int(dict[s[i+1]])
            calc , skip= self.rules(nr, nr_next)
            result += calc
        return result



sol = Solution().romanToInt("III")
print(sol)
sol2 = Solution().romanToInt("LVIII")
print(sol2)
sol3 = Solution().romanToInt("MCMXCIV")
print(sol3)
