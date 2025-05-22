# sort colors
# dutch national flag

class Solution(object):
    def sortColors(self, nums):
        s,m,e = 0,0,len(nums)-1
        while m<=e:
            if nums[m] == 0:
                nums[s],nums[m] = nums[m],nums[s]
                s = s+1
                m = m+1
            elif nums[m] == 1:
                 m = m+1
            else:
                nums[m],nums[e] = nums[e],nums[m]
                e = e-1