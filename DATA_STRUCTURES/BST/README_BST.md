## BINARY SEARCH TREE

BSTs are similar to arrays in that the stored values (the “keys”) are stored in a sorted order.
However, unlike with a sorted array, keys can be added to and deleted from a BST efficiently.
Avoid mutating objects in a BST. Remove it, update it and then add it back.

Properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.

Two strategies to traverse:

- DFS (Preorder, Inorder, Postorder)
- BFS

### Time:
`O(log N)` in general

### Python:
  - `bintrees` library
  - `insert(e)`
  - `discard(e)` removes e if present
  - `min_item()` and `max_item()` key-value
  - `min_key()` and `max_key()` key
  - `pop_min()` and `pop_max()` remove and return key-value pair
