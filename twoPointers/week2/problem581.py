# shortest unsorted continuous subarray

class Solution(object):
    def findUnsortedSubarray(self, nums):
        left,right = 0,len(nums)-1
        
        if len(nums) == 1:
            return 0
        while left< len(nums)-1 and nums[left] <= nums[left+1]:
                left+=1
                
            
        if left == len(nums)-1:
                return 0    
        while right> 0 and nums[right] >= nums[right-1]:
                right-=1
        min_val = min(nums[left:right + 1])
        max_val = max(nums[left:right + 1])
        
        
        while left > 0 and nums[left - 1] > min_val:
            left -= 1
        
        
        while right < len(nums) - 1 and nums[right + 1] < max_val:
            right += 1        
        
        return right-left+1