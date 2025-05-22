# sort the array by parity2
# even numbers in even indices and odd numbers in odd indices

class Solution(object):
    def sortArrayByParityII(self, nums):
        l,r = 0,1
        while l < len(nums) and r < len(nums):
            if nums[l]%2 == 0:
                l = l+2
            elif nums[r]%2!= 0:
                r = r-2
            else:
                nums[l],nums[r] = nums[r],nums[l]
        return nums     