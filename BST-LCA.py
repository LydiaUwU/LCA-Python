# @Author: Lydia MacBride, 19333944
#
# Implementation of LCA in python for Software Engineering module
# Heavily based on these posts:
#  - https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#  - https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
#
# I love my wives

# BST class
class BST:
    # Constructor
    def __init__(self):
        self.root = None

    # Call get_node()
    def get_node(self, key):
        return self.get_node_rec(self.root, key)

    # Get node from tree
    def get_node_rec(self, root, key):
        # Base cases where root is null or search matches root
        if self.root is None or self.root.key == key:
            return self.root

        # Greater than root's key
        if key > self.root.key:
            self.get_node_rec(root.right, key)

        # Less than root's key
        return self.get_node_rec(root.left, key)

    # Call add_node()
    def add_node(self, key):
        self.root = self.add_node_rec(self.root, key)

    # Add node to tree
    def add_node_rec(self, node, key):
        # Return new node if tree is empty
        if node is None:
            node = Node(key)
            return node

        # Else recur through tree
        if key < node.key:
            node.left = self.add_node_rec(node.left, key)
        else:
            node.right = self.add_node_rec(node.right, key)

        # Return unchanged node
        return node

    # Calls lca_rec()
    def lca(self, n1, n2):
        return self.lca_rec(self.root, n1, n2)

    def lca_rec(self, node, n1, n2):
        # Return None if tree is empty
        if node is None:
            return None

        # If both n1 and n2 are smaller than root
        if node.key > n1 and node.key > n2:
            return self.lca_rec(node.left, n1, n2)

        # If both n1 and n2 are greater than root
        if node.key < n1 and node.key < n2:
            return self.lca_rec(node.right, n1, n2)

        # Else return node
        return node

    pass


# Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    pass


# Main
# Initialise tree
tree = BST()

# Create following BST
#           50
#        /     \
#      30      70
#     /  \     /  \
#    20   40  60   80
tree.add_node(50)
tree.add_node(30)
tree.add_node(20)
tree.add_node(40)
tree.add_node(70)
tree.add_node(60)
tree.add_node(80)

# Example lca() call
print("LCA of 20 and 40: " + str(tree.lca(20, 40).key))
