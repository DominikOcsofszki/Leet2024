class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            # if nums[i] == target:
            #     return i
            if nums[i] >= target:
                if nums[i] == target:
                    return i
                return i- 1