class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        back = s[::-1]
        back.strip()
        print(back)
        for i in range(len(back)):
            if back[i] is not ' ':
                return i
        

