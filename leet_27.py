class Solution1:
    def removeElement(self, nums: list[int], val: int) -> int:
        while nums.__contains__(val):
            nums.remove(val)
        return len(nums)
    
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = 999
#         return len(nums)-count
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if not nums[i] == val:
                nums[index] = nums[i]
                index +=1
        return index
nums =[0,1,2,2,3,0,4,2]
res =Solution().removeElement(nums, 2)
print(res)