"""
Design a data structure that follows the constraints of a 
Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache 
with positive size capacity.

int get(int key) Return the value of the key 
if the key exists, otherwise return -1.

void put(int key, int value) Update the value 
of the key if the key exists. Otherwise, add 
the key-value pair to the cache. If the number 
of keys exceeds the capacity from this operation, 
evict the least recently used key.

Time Complexity: O(1)
Space: O(capacity)
"""


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self.remove_node(node)
            self.add_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        existing = self.cache.get(key)
        if not existing:
            new_node = Node(key, value)
            self.add_node_to_head(new_node)
            self.cache[key] = new_node
            self.size += 1
            if self.size > self.capacity:
                to_remove = self.tail.prev
                self.remove_node(to_remove)
                del self.cache[to_remove.key]
                self.size -= 1
        else:
            self.remove_node(existing)
            self.add_node_to_head(existing)
            existing.val = value

    def add_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev