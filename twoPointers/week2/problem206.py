# reverse a singly linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
       
        prev,temp= None,head
        while temp:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        return prev