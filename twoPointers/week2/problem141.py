# linked list cycle detection

class Solution(object):
    def hasCycle(self, head):
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
                if fast==slow:
                    return True
        return False