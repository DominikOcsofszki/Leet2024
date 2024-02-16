class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        arr =[]
        for x in s:
            if x in dict.keys():
                arr.append(x)
            else:
                if x in dict.values():
                    if len(arr) == 0:
                        return False
                    out = arr.pop()
                    # print(out)
                    if x is not dict[out]:
                        return False
        return len(arr) == 0
    
print(Solution().isValid("{}"))
print(Solution().isValid("{a]}"))
print(Solution().isValid("{[a]}"))
print(Solution().isValid("{b}"))
print(Solution().isValid("{b}"))