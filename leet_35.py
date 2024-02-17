class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums)
        for i in range(end):
            if nums[i] >= target:
                return i
        return end