class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head: ListNode):  # Iterative
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


def reverse_list_recursive(head: ListNode):  # Recursive
    if not head or not head.next:
        return head
    # This step takes us to then end
    p = reverse_list_recursive(head.next)
    # Process the current node
    # Make the next node to point to the current
    head.next.next = head
    head.next = None
    # Always return the last node, which will be the first node
    return p


def reverse_sublist(head: ListNode, m: int, n: int) -> ListNode:
    """
    Reverse a linked list from position m to n. Do it in one-pass
    """
    if not head or m == n:
        return head
    prev, current = None, head
    i = 1
    while current and i < m:
        prev, current = current, current.next
        i += 1
    # at this point, current is the first element
    # wee need to store these nodes to make a connection
    # at the end
    last_node_of_first_part = prev
    first_node_of_second_part = current

    while current and i < n + 1:
        current.next, prev, current = prev, current, current.next
        i += 1
    # at this point current is the first element after
    # the reversed section
    if last_node_of_first_part:
        last_node_of_first_part.next = prev
    else:
        head = prev
    first_node_of_second_part.next = current
    return head
