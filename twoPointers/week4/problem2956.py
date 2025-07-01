# find intersection values in two arrays
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2 = {}
        result = []
        for i in nums1:
            dict1[i] = 1 + dict1.get(i,0)
        for i in nums2:
            dict2[i] = 1 + dict2.get(i,0)
        left,right = 0,0    
        for i in nums1:
            if i in nums2:
                left+=1
        
               
        for i in nums2:
            if i in nums1:
                right+=1        
        result.append(left)
        result.append(right)
        return result
        