# LeetCode 219. Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # dict1 = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dict1:
        #         dict1[nums[i]] = i
        #     else:
        #         diff = abs(i - dict1[nums[i]])
        #         if diff <= k:
        #             return True
        #         else:
        #             dict1[nums[i]] = i    
        # return False    

        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            
            set1.add(nums[i])
            if len(set1) > k:
                    set1.remove(nums[i-k])
        return False