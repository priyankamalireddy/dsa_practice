# apply operations to an array
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        # read,write = 0,1
        # while write < len(nums) and read <= write:
        #     if nums[read] == 0 and nums[write] == 0:
        #         write+=1
        #     elif nums[read] == 0:
        #         nums[read],nums[write] = nums[write],nums[read]
        #         read+=1
        #         write+=1
        #     else:
        #         read+=1
        #         write+=1
        # return nums                 
        result = []
        count = 0
        for i in nums:
            if i == 0:
                count+=1
            else:
                result.append(i)
        for _ in range(count):
            result.append(0) 
        return result            