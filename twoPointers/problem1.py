# two sum
class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        for i,num in enumerate(nums):
            c = target - num
            if c in dict1:
                return(dict1[c],i)
            dict1[num] = i
h1 = Solution()
print(h1.twoSum([3,3],6))