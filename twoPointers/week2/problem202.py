# happy number

class Solution(object):
    def isHappy(self, n):
        def squared_sum(n):
            sum = 0
            while n > 0:
                a = n %10
                sum+= a**2
                n = n//10
            return sum
        seen = set()
        # while n > 0:
        #     n = squared_sum(n)
        #     if n == 1:
        #         return True
        #     if n in seen:
        #         return False
        #     else:
        #         seen.add(n)    
        slow = n
        fast = squared_sum(n)
        while fast!=1 and slow!=fast:
            slow = squared_sum(slow)
            fast = squared_sum(squared_sum(fast))
        return fast==1 