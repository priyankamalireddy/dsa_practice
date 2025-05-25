from typing import (
    List,
)

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        
            nums = sorted(nums)
            count = 0
            for i, num in enumerate(nums):
                j,k = i+1,len(nums)-1
                while j<k:
                    res = num + nums[j] + nums[k]
                    if res < target:
                        count+= (k-j)
                        j+=1
                    else:
                        
                        k-=1    
            return count
