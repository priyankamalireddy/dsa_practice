# longest harmonious subsequence

class Solution(object):
    def findLHS(self, nums):
        result = []
        dict1 = {}
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        for i in nums:
            if i+1 in dict1:
                frequency = dict1[i] + dict1[i+1]
                result.append(frequency)
        if len(result) == 0:
            return 0        
        return max(result)