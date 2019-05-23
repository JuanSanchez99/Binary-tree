class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} -- (l - {} r - {})".format(self.val, self.left, self.right)


def show(tree):
    print(tree)


def push_node(tree, val):
    if tree is None:
        return Node(val)
    if val < tree.val:
        return Node(tree.val, push_node(tree.left, val), tree.right)

    return Node(tree.val, tree.left, push_node(tree.right, val))


def to_tree(lst, tree=None):
    if not lst:
        return tree
    return to_tree(lst[1:], push_node(tree, lst[0]))


if __name__ == '__main__':
    print(push_node(
        Node(25, Node(18, Node(10), Node(20)), Node(50, Node(40))),
        45
    ))

    print(to_tree([25, 18, 50, 10, 20, 40]))
