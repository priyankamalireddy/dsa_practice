# linked list cycle II

def detectCycle(self, head):
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                curr = head
               
                while curr!= slow:
                    curr = curr.next
                    slow = slow.next
                return slow
        return None           
        