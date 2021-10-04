# @Author: Lydia MacBride, 19333944
#
# Main script to demonstrate functionality of bst.py

import bst

# Main
# Initialise tree
tree = bst.BST()

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