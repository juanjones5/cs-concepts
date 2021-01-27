"""
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the 
nodes of the first two lists.
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_iterative(l1: Node, l2: Node) -> Node:
    prehead = Node()
    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            prev, l1 = l1, l1.next
        else:
            prev.next = l2
            prev, l2 = l2, l2.next
    prev.next = l1 if l1 is not None else l2
    return prehead.next


def merge_recursive(l1: Node, l2: Node) -> Node:
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val <= l2.val:
        l1.next = merge_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_recursive(l1, l2.next)
        return l2