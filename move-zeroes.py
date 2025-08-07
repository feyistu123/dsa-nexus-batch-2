class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold = 0  
        seek = 0
        for seek in range(len(nums)):
            if nums[seek] != 0:
                nums[hold], nums[seek] = nums[seek], nums[hold]
                hold += 1
