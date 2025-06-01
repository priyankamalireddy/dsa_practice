#palindrome-linked-list 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
            
            slow = head
            fast = head
            while fast and fast.next!=None:
                slow = slow.next
                fast = fast.next.next
            prev = None
            while slow:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            n1,n2 = head,prev
            while n2:
                if n1.val!=n2.val:
                    return False
                n1 = n1.next
                n2 = n2.next
            return True  