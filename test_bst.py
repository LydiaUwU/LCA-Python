# @Author: Lydia MacBride, 19333944
#
# Unit testing of methods in bst.py
#
# I love my wives

from unittest import TestCase

import bst


class TestBST(TestCase):
    # ~~~~~~~~~~ Test constructors ~~~~~~~~~~
    # test_ Node constructor
    def test_node_constructor(self):
        node = bst.Node(1)

        self.assertEqual(1, node.key)

    # test_ BST constructor
    def test_bst_constructor(self):
        tree = bst.BST()

        self.assertEqual(None, tree.root)

    # ~~~~~~~~~~ Test get_node() ~~~~~~~~~~
    # Where root is null
    def test_get_node_none(self):
        tree = bst.BST()

        self.assertEqual(None, tree.get_node(1))

    # Where search key doesn't exist
    def test_get_node_none_key(self):
        tree = bst.BST()
        tree.add_node(1)

        self.assertEqual(None, tree.get_node(2))

    # Where root is equal to search key
    def test_get_node_same_key(self):
        tree = bst.BST()
        tree.add_node(1)

        self.assertEqual(1, tree.get_node(1).key)

    # Where search key is greater than root
    def test_get_node_key_gd(self):
        tree = bst.BST()
        tree.add_node(1)  # Root
        tree.add_node(2)

        self.assertEqual(2, tree.get_node(2).key)

    # Where search key is less than root
    def test_get_node_key_ld(self):
        tree = bst.BST()
        tree.add_node(2)  # Root
        tree.add_node(1)

        self.assertEqual(1, tree.get_node(1).key)

    # ~~~~~~~~~~ Test add_node() ~~~~~~~~~~
    # Add one node to tree
    def test_add_node(self):
        tree = bst.BST()
        tree.add_node(10)

        self.assertEqual(10, tree.get_node(10).key)

    # Check that values > root and vales < root are added correctly
    def test_add_node_3(self):
        tree = bst.BST()
        tree.add_node(2)  # Root
        tree.add_node(1)
        tree.add_node(3)

        self.assertEqual(tree.get_node(1), tree.get_node(2).left)
        self.assertEqual(tree.get_node(3), tree.get_node(2).right)

    # Check adding a child, and then its own child
    def test_grandchild(self):
        tree = bst.BST()
        tree.add_node(3)  # Root
        tree.add_node(2)  # Child
        tree.add_node(1)  # Grandchild

        self.assertEqual(tree.get_node(1), tree.get_node(3).left.left)

    # ~~~~~~~~~~ test_ lca() ~~~~~~~~~~
    # Where root is null
    def test_lca_none(self):
        tree = bst.BST()

        self.assertEqual(None, tree.lca(1, 2))

    # Where root is LCA and there are 3 nodes
    def test_lca_3(self):
        tree = bst.BST()
        tree.add_node(2)  # Root and LCA
        tree.add_node(1)
        tree.add_node(3)

        self.assertEqual(tree.get_node(2), tree.lca(1, 3))

    # Where LCA lies to left of root
    def test_lca_left(self):
        tree = bst.BST()
        tree.add_node(4)  # Root
        tree.add_node(2)  # LCA
        tree.add_node(1)
        tree.add_node(3)

        self.assertEqual(tree.get_node(2), tree.lca(1, 3))

    # Where LCA lies to right of root
    def test_lca_right(self):
        tree = bst.BST()
        tree.add_node(1)  # Root
        tree.add_node(3)  # LCA
        tree.add_node(2)
        tree.add_node(4)

        self.assertEqual(tree.get_node(3), tree.lca(2, 4))

    pass
