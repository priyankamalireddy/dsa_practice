# subarray-product-less-than-k
# given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = 0
        count = 0
        product = 1
        for right in range(len(nums)):
            product*= nums[right]
            while product >= k:
                product//= nums[left]    
                left+=1
            count+= (right-left+1)    
        return count