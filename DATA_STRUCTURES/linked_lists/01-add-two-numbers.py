"""
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit. Add the two numbers and return the 
sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode()
        current = result
        while l1 or l2:
            current_sum = (carry + (l1.val if l1 else 0) + (l2.val if l2 else 0))
            carry = 1 if current_sum > 9 else 0
            value_to_add = current_sum % 10
            current.next = ListNode(value_to_add)
            current = current.next
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)
        # IMPORTANT - CHECK IF WE NEED TO ADD FROM THE CARRY
        if carry == 1:
            current.next = ListNode(1)
        return result.next