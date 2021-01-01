class Solution(object):        
    def reverse_list(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
    def reverse_list_recursive(self, head):  # Recursive   
        if not head or not head.next:
            return head
        # This step takes us to then end
        p = self.reverse_list_recursive(head.next)
        # Process the current node
        # Make the next node to point to the current
        head.next.next = head
        head.next = None
        # Always return the last node, which will be the first node
        return p
