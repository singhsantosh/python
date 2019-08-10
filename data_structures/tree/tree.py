class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


a = ['a', 'c', 'c', 'd', 'e', 'f', 'g', 'h']

assert a[5:] == a[5:len(a)]
