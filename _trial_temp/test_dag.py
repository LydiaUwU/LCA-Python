# @Author: Lydia MacBride, 19333944
#
# Unit testing of methods in dag.py
#
# I love my wives

from unittest import TestCase

import dag


class TestDAG(TestCase):
    # ~~~~~~~~~~ Test constructors ~~~~~~~~~~
    # test_ Node constructor
    def test_node_constructor(self):
        node = dag.Node(1, [None])

        self.assertEqual(1, node.key)

    # test_ DAG constructor
    def test_dag_constructor(self):
        tree = dag.DAG()

        self.assertEqual(None, tree.root)

    # ~~~~~~~~~~ Test get_node() ~~~~~~~~~~
    # Where root is null
    def test_get_node_none(self):
        tree = dag.DAG()

        self.assertEqual(None, tree.get_node(1))

    # Where search key doesn't exist
    def test_get_node_none_key(self):
        tree = dag.DAG()
        tree.add_node(1, [None])

        self.assertEqual(None, tree.get_node(2))

    # Where root is equal to search key
    def test_get_node_same_key(self):
        tree = dag.DAG()
        tree.add_node(1, [None])

        self.assertEqual(1, tree.get_node(1).key)
        self.assertEqual(0, tree.get_node(1).depth)

    # Test where search key has depth 1
    def test_get_1_depth(self):
        tree = dag.DAG()
        tree.add_node(1, [None])
        tree.add_node(2, [1])

        self.assertEqual(2, tree.get_node(2).key)
        self.assertEqual(1, tree.get_node(2).depth)

    # Test where search key has depth 2
    def test_get_2_depth(self):
        tree = dag.DAG()
        tree.add_node(1, [None])
        tree.add_node(2, [1])
        tree.add_node(3, [2])

        self.assertEqual(3, tree.get_node(3).key)
        self.assertEqual(2, tree.get_node(3).depth)

    # Test where search key has two parents
    def test_get_2_parents(self):
        tree = dag.DAG()
        tree.add_node(1, [None])
        tree.add_node(2, [1])
        tree.add_node(3, [1, 2])

        self.assertEqual(3, tree.get_node(3).key)

    # ~~~~~~~~~~ Test add_node() ~~~~~~~~~~
    # Add one node to tree
    def test_add_node(self):
        tree = dag.DAG()
        tree.add_node(10, [0])

        self.assertEqual(10, tree.get_node(10).key)

    # Check that values > root and vales < root are added correctly
    def test_add_node_3(self):
        tree = dag.DAG()
        tree.add_node(2, [None])  # Root
        tree.add_node(1, [2])
        tree.add_node(3, [2])

        self.assertEqual(tree.get_node(1), tree.get_node(2).children[0])
        self.assertEqual(tree.get_node(3), tree.get_node(2).children[1])

    # Check adding a child, and then its own child
    def test_add_grandchild(self):
        tree = dag.DAG()
        tree.add_node(3, [None])   # Root
        tree.add_node(2, [3])  # Child
        tree.add_node(1, [2])  # Grandchild

        self.assertEqual(tree.get_node(1), tree.get_node(3).children[0].children[0])

    # ~~~~~~~~~~ Test lca() ~~~~~~~~~~
    # Where root is null
    def test_lca_none(self):
        tree = dag.DAG()

        self.assertEqual(None, tree.lca(1, 2))

    # Search nodes are equal
    def test_lca_same(self):
        tree = dag.DAG()
        tree.add_node("root", [None])
        tree.add_node("a", ["root"])

        self.assertEqual(tree.get_node("a").key, tree.lca("a", "a"))

    # First search node is root
    def test_lca_first_root(self):
        tree = dag.DAG()
        tree.add_node("root", [None])
        tree.add_node("a", ["root"])

        self.assertEqual(tree.get_node("root").key, tree.lca("root", "a"))

    # Second search node is root
    def test_lca_second_root(self):
        tree = dag.DAG()
        tree.add_node("root", [None])
        tree.add_node("a", ["root"])

        self.assertEqual(tree.get_node("root").key, tree.lca("a", "root"))

    # Where root is LCA and there are 3 nodes
    def test_lca_3(self):
        tree = dag.DAG()
        tree.add_node("root", [None])  # Root and LCA
        tree.add_node("a", ["root"])
        tree.add_node("b", ["root"])

        self.assertEqual(tree.get_node("root"), tree.lca("a", "b"))

    # Where LCA is at 1 depth
    def test_lca_1_depth(self):
        tree = dag.DAG()
        tree.add_node("root", [None])  # Root
        tree.add_node("lca", ["root"])  # LCA
        tree.add_node("a", ["lca"])
        tree.add_node("b", ["lca"])

        self.assertEqual(tree.get_node("lca").key, tree.lca("a", "b").key)

    # Where LCA at 0 depth but nodes at 2 depth
    def test_lca_deep(self):
        tree = dag.DAG()
        tree.add_node("root", [None])
        tree.add_node("x", ["root"])
        tree.add_node("y", ["root"])
        tree.add_node("a", ["x"])
        tree.add_node("b", ["y"])

        self.assertEqual(tree.get_node("root").key, tree.lca("a", "b").key)

    # Where LCA at 1 depth but nodes at 3 depth
    def test_lca_deep_2(self):
        tree = dag.DAG()
        tree.add_node("root", [None])
        tree.add_node("lca", ["root"])
        tree.add_node("x", ["lca"])
        tree.add_node("y", ["lca"])
        tree.add_node("a", ["x"])
        tree.add_node("b", ["y"])

        self.assertEqual(tree.get_node("lca").key, tree.lca("a", "b").key)

    # Where there are two LCAs at different depths
    def test_lca_2_lca(self):
        tree = dag.DAG()
        tree.add_node("root", [None])  # Root
        tree.add_node("lca1", ["root"])  # LCA1
        tree.add_node("lca2", ["root"])
        tree.add_node("a", ["lca1", "lca2"])
        tree.add_node("b", ["lca1", "lca2"])

        self.assertEqual(tree.get_node("lca1"), tree.lca("a", "b"))

    pass
