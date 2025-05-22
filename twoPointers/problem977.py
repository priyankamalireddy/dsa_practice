#squares of a sorted array
class Solution(object):
    def sortedSquares(self, nums):
        l,r = 0,len(nums)-1
        result = []
        while l <= r:
            if nums[l]**2 >= nums[r]**2:
                result.append(nums[l]**2)
                l = l+1
            else:
                result.append(nums[r]**2)
                r = r-1    
        return result[::-1]         
s1 = Solution()
s1.sortedSquares([-5,-3,-2,-1])