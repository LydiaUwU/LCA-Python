# @Author: Lydia MacBride. 19333944
#
# Implementation of a Directed Acyclic Graph in Python
#
# I love my wives

# DAG Class
class DAG:
    def __init__(self):
        self.root = None

    # Add node to DAG
    def add_node(self, key, parents):
        if self.root is None:
            self.root = Node(key, [None])
            self.root.set_depth(0)
        else:
            # Generate parents from keys
            parent_nodes = list()

            for i in parents:
                parent_node = self.get_node(i)
                if i is not None:
                    parent_nodes.append(parent_node)

            new_node = Node(key, parent_nodes)
            self.add_node_rec(new_node, self.root, 1)

    # Recursive helper function to add_node()
    def add_node_rec(self, new_node, search_node, depth):
        if search_node in new_node.parents:
            new_node.set_depth(depth)
            search_node.add_child(new_node)

        for node in search_node.children:
            self.add_node_rec(new_node, node, depth + 1)

    # Find a node in the DAG
    def get_node(self, key):
        if self.root is None:
            return None

        if self.root.key == key:
            return self.root

        return self.get_node_rec(self.root, key)

    # Recursive helper function to get_node()
    def get_node_rec(self, search_node, key):
        if search_node.key == key:
            return search_node
        elif len(search_node.children) > 0:
            for node in search_node.children:
                ret_node = self.get_node_rec(node, key)
                if ret_node is not None:
                    return ret_node

        return None

    # Find the lowest common ancestor of two nodes
    def lca(self, key_1, key_2):
        if self.root is None:
            return None

        if key_1 == key_2 or key_1 == self.root.key:
            return key_1
        elif key_2 == self.root.key:
            return key_2

        return self.lca_rec(self.get_node(key_1), self.get_node(key_2))

    # Recursive helper function to lca()
    def lca_rec(self, node_1, node_2):
        # Case 1: Check if nodes are None
        if node_1 is None or node_2 is None:
            return self.root

        # Case 2: Parents of node_1 against parent of node_2
        common_nodes = list()

        for node in node_1.parents:
            if node in node_2.parents and node not in common_nodes and node is not None:
                common_nodes.append(node)

        # Case 3: Grandparents of node_1 against node_2
        for node in node_1.parents:
            new_node = self.lca_rec(node, node_2)
            if new_node not in common_nodes and new_node is not None:
                common_nodes.append(new_node)

        # Case 4: Parents of node_1 against grandparents of node_2
        for node in node_2.parents:
            new_node = self.lca_rec(node_1, node)
            if new_node not in common_nodes and new_node is not None:
                common_nodes.append(new_node)

        # Find common node with highest depth
        max_depth_node = self.root

        for node in common_nodes:
            if node is not None:
                if node.depth > max_depth_node.depth:
                    max_depth_node = node

        return max_depth_node

    pass


# Node class for DAG
class Node:
    # Constructor
    def __init__(self, key, parents):
        self.key = key
        self.parents = parents
        self.children = list()
        self.depth = None

    def add_child(self, child):
        self.children.append(child)

    def set_depth(self, depth):
        self.depth = depth

    pass
