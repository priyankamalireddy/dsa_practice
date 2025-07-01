# Given a string s, reverse only all the vowels in the string and return it.
class Solution(object):
    def reverseVowels(self, s):
        # r=""
        # l=[]
        # j=0
        # for i in s:
        #     if i in "aeiouAEIOU":
        #         l.append(i)
        #     else:
        #         pass 
        # nl=l[: :-1]
        # for i in s:
        #     if i in "aeiouAEIOU":
        #         r+=nl[j]
        #         j+=1
        #     else:    
        #         r+= i
        # return r  
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l, r = 0, len(s)-1
        l_s = list(s)
        while l<=r:
            if l_s[l] in vowels and l_s[r] in vowels:
                l_s[l],l_s[r] = l_s[r],l_s[l]
                l+=1
                r-=1
            elif l_s[l] in vowels and l_s[r] not in vowels:
                r-=1
            elif l_s[l] not in vowels and l_s[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(l_s)  