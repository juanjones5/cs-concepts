class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head: Node, insertVal: int) -> Node:
    """
    Given a node from a Circular Linked List which is sorted
    in ascending order, write a function to insert a value
    insertVal into the list such that it remains a sorted
    circular list. The given node can be a reference to any
    single node in the list, and may not be necessarily
    the smallest value in the circular list.

    If there are multiple suitable places for insertion,
    you may choose any place to insert the new value.
    After the insertion, the circular list should remain sorted.

    Time Complexity: O(N)
    Space: O(1)
    """
    # case 1: the list is empty
    if not head:
        node = Node(insertVal)
        node.next = node
        return node

    def insert_between(n1, n2):
        new_node = Node(insertVal)
        n1.next, new_node.next = new_node, n2
        return head

    prev, curr = head, head.next
    while True:
        # case 2: we find a spot in between
        if prev.val <= insertVal and insertVal <= curr.val:
            return insert_between(prev, curr)
        # case 3: our value is bigger than the max or smaller than the min
        elif curr.val < prev.val and (insertVal >= prev.val or insertVal <= curr.val):
            return insert_between(prev, curr)
        prev, curr = curr, curr.next
        # case 4: the list has a single value or all duplicate values
        if prev == head:
            break
    head.next = Node(insertVal, curr)
    return head