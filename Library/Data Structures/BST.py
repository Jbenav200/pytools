# Content originally learned at GeeksForGeeks
# A Binary Search Tree in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Insert a value into the tree.
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# In order tree traversal
def traverse_in_order(root):
    if root:
        traverse_in_order(root.left)
        print(root.val)
        traverse_in_order(root.right)


# Search for a value in the tree.
def search(root, key):
    # Base Cases: root is null or key is present at root.
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)
