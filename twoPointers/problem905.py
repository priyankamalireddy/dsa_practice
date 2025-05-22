#sorting the array by parity
#even numbers followed by odd numbers

class Solution(object):
    def sortArrayByParity(self, nums):
        
        l,r = 0,len(nums)-1
        while l <= r:
            if nums[r]%2 == 0 and nums[l]%2!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l = l+1
                r = r-1
            elif nums[l]%2 == 0:
                l = l+1
            elif nums[r]%2 != 0:
                r = r-1
        return nums