#4sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final = []
        nums = sorted(nums)
        if len(nums) < 4:
            return final
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j >i+1 and nums[j] == nums[j-1]:
                    continue
                h_t = nums[i] + nums[j]
                k,l = j+1, len(nums)-1
                while k<l:
                    result = nums[k]+nums[l]
                    if h_t + result == target:
                        final.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k+= 1  

                        while k < l and nums[l] == nums[l - 1]:
                            l-= 1  
                        k+=1    
                    elif h_t + result < target:
                        k+=1
                    elif h_t + result > target:
                        l-=1    
        return final