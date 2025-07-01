# Problem 350. Intersection of Two Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for i in nums1:
            dict1[i] = 1 + dict1.get(i,0)
        dict2 = {}
        for i in nums2:
            dict2[i] = 1 + dict2.get(i,0)
        result = []
        for i in dict1:
            if i in dict2:
                min1 = min(dict1[i],dict2[i])
                while min1 > 0:
                    result.append(i)
                    min1-=1
        return result                    