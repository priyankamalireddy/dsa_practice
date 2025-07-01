# Problem 283: Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 1
        while write < len(nums) and read <= write:
            if nums[read] == 0 and nums[write] == 0:
                write+=1
            elif nums[read] == 0:
                nums[read],nums[write] = nums[write],nums[read]
                read+=1
                write+=1
            else:
                read+=1
                write+=1        