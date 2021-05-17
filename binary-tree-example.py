class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        # declare and define nodes of the tree
        self.root = Node(val=13)
        self.n2 = Node(val=12)
        self.n3 = Node(val=34)
        self.n4 = Node(val=7)
        self.n5 = Node(val=15)
        self.n6 = Node(val=89)

        # define the relationship between nodes
        self.root.left = self.n2
        self.root.right = self.n3
        self.n2.left=self.n4
        self.n2.right=self.n5
        self.n3.right=self.n6

        print('The sum of all nodes within this tree is {}'.format(self.calc_tree_sum(node=self.root)))
        print()

    def calc_tree_sum(self, node):
        # assume that we are given the root node of the tree as starting point
        # make use of recursion
        # base case
        if node == None:
            return 0
        # recursive case
        else:
            return node.val + self.calc_tree_sum(node.left) + self.calc_tree_sum(node.right)


BinaryTree()