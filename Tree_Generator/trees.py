# Binary Search Tree (BST)
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                # recursion for tree traversal
                self.left.insert(data)
            else:
                # child node insertion
                self.left = Tree(data)
                return
        else:
            if self.right:
                # recursion for tree traversal
                self.right.insert(data)
            else:
                # child node insertion
                self.right = Tree(data)
                return
