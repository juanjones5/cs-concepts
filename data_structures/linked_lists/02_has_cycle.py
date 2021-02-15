class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def has_cycle(self, head: Node) -> bool:
    if not head:
        return False
    slow, fast = head, head.next
    while fast:
        if fast == slow:
            return True
        slow = slow.next
        if fast.next is None:
            break
        fast = fast.next.next
    return False