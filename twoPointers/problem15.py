#three sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        for i,a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,len(nums)-1
            while j<k:
                sum1 = nums[j]+nums[k]+a
                
                if sum1 == 0:
                   
                    result.append([a,nums[j],nums[k]])
                    j = j+1
                    while nums[j] == nums[j-1] and j<k:
                        j = j+1
                elif sum1 < 0:
                    j = j+1
                else:
                    k = k-1 
        return result
