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
    def get_node_rec(self, node, key):
        # Base cases where node is null or search matches node
        if node is None or node.key == key:
            return node

        # Greater than node's key
        if key > node.key:
            return self.get_node_rec(node.right, key)

        # Less than node's key
        return self.get_node_rec(node.left, key)

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
