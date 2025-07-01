# Problem 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a,b = headA,headB
        if not headA or not headB:
            return None    
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
        