'''移动零
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。
注意事项:
    必须在原数组上操作，不要为一个新数组分配额外空间。
    尽量减少操作总数。
'''
#把不是零的数往前面压缩，然后后边全置零就完了
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len1 = len(nums)
        j = 0
        for i in range(len1):
            if nums[i] != 0:
                nums[j] = nums[i]
                j = j+1
        for k in range(j, len1):
            nums[k] = 0
