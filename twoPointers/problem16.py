# threeSumClosest
# Given an integer array nums of length n and an integer target,
# return the sum of three integers in nums such that it is closest to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# The solution should be in O(n^2) time complexity.


class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i,a in enumerate(nums):
            j,k = i+1,len(nums)-1
            while j<k:
                closest_sum = a + nums[j]+nums[k]

                if closest_sum < target:
                    j = j+1
                elif closest_sum > target:
                    k = k-1
                else:
                    return closest_sum 
                if abs(closest_sum-target) < abs(result - target):
                    result = closest_sum 
                     
                          
        return result