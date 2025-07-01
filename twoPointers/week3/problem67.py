# Add binary numbers
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j = len(a)-1,len(b)-1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >=0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            sum1 = digit_a + digit_b + carry
            result.append(str(sum1 % 2))
            carry = sum1 // 2
            i-= 1
            j-= 1    
            
        return ''.join(reversed(result))               