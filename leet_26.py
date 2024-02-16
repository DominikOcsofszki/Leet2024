class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 1
        for i in range(len_nums - 1):
            if i == len_nums:
                continue
            if nums[i] == nums[i + 1]:
                nums[i] = 999
        nums.sort()
        count_ = nums.count(999)
        return  len_nums - count_
test1 = [1,1,2]
test2 = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(test1))
print(Solution().removeDuplicates(test2))