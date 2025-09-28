# search in rotated array 2

class Solution(object):
    def search(self, nums, target):
        low, high = 0,len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[low] > nums[mid]:

                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                low+=1        
        return False                               

        