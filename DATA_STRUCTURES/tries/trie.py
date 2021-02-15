class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        # True if node represents the end of the word
        self.is_end = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        current_node = self.root
        for level in range(len(key)):
            index = ord(key[level]) - ord("a")
            # if current character is not present
            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]
        # mark last node as leaf
        current_node.is_end = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key is present
        # in trie, else false
        current_node = self.root
        for level in range(len(key)):
            index = ord(key[level]) - ord("a")
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        return current_node != None and current_node.is_end