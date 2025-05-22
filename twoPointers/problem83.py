#remove duplicates from sorted list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        l1 = []
        prev = None
        curr = head
        while curr!=None:
            if curr.val not in l1:
                l1.append(curr.val)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
                
        return head 