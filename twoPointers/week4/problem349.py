# Given two arrays, write a function to compute their intersection.
# Each element in the result must be unique.
class Solution(object):
    def intersection(self, nums1, nums2):
        dict1 = {}
        for i in nums1:
            dict1[i] = 1 + dict1.get(i,0)
        dict2 = {}
        for i in nums2:
            dict2[i] = 1 + dict2.get(i,0)
        result = []
        for i in dict1:
            if i in dict2:
                result.append(i)
        return result                
                 
