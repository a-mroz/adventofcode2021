import fileinput
import math
import copy
import datetime

class Node:
    def __init__(self, parent, value = None, left = None, right = None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value and self.right == other.right and self.left == other.left


    def __str__(self):
        if type(self.value) is int:
            return str(self.value)

        return '[' + str(self.left) + ',' + str(self.right) + ']'

def parse_file():
    return [parse_tree(l.strip()) for l in fileinput.input()]

def parse_tree(line):
    lst = eval(line)

    root = Node(None)
    root.left = parse_node_rec(root, lst[0])
    root.right = parse_node_rec(root, lst[1])
    return root


def parse_node_rec(parent, lst):
    node = Node(parent)

    if type(lst) is int:
        node.value = lst
    else:
        left = parse_node_rec(node, lst[0])
        node.left = left

        right = parse_node_rec(node, lst[1])
        node.right = right

    return node

def add(t1, t2):
    new_tree = Node(None)
    new_tree.left = t1
    new_tree.right = t2
    t1.parent = new_tree
    t2.parent = new_tree
    return new_tree

def reduce(tree):
    any_action = True

    while any_action:
        exploded = True
        while exploded:
            exploded = explode(tree)

        splitted = split(tree)

        any_action = exploded or splitted

def explode(tree, level = 0):
    if tree is None or (type(tree.value) is int and level < 4):
        return False

    if level == 4 and tree.left is not None and tree.right is not None:
        assert type(tree.left.value) is int
        assert type(tree.right.value) is int
        add_x_to_elem_on_left(tree, tree.left.value)
        add_x_to_elem_on_right(tree, tree.right.value)

        tree.value = 0
        tree.left = None
        tree.right = None

        return True
    else:
        exploded = explode(tree.left, level + 1)
        if not exploded:
            exploded = explode(tree.right, level + 1)
        return exploded

def add_x_to_elem_on_left(tree, value):
    left_subtree = find_left_subtree(tree)
    if left_subtree:
        rightmost = find_rightmost_leaf(left_subtree)
        if rightmost:
            rightmost.value += value


def find_left_subtree(tree):
    parent = tree.parent

    # root
    if parent.parent is None:
        return parent.left if parent.left is not tree else None

    if parent.left is tree:
        return find_left_subtree(parent)
    return parent.left


def find_rightmost_leaf(tree):
    if tree is None or type(tree.value) is int:
        return tree

    l = find_rightmost_leaf(tree.right)

    return l if l else find_rightmost_leaf(tree.left)



def add_x_to_elem_on_right(tree, value):
    right_subtree = find_right_subtree(tree)
    if right_subtree:
        leftmost = find_leftmost_leaf(right_subtree)
        if leftmost:
            leftmost.value += value


def find_right_subtree(tree):
    parent = tree.parent
    # root
    if parent.parent is None:
        return parent.right if parent.right is not tree else None

    if parent.right is tree:
        return find_right_subtree(parent)
    return parent.right


def find_leftmost_leaf(tree):
    if tree is None or type(tree.value) is int:
        return tree

    l = find_leftmost_leaf(tree.left)

    return l if l else find_leftmost_leaf(tree.right)


def split(tree):
    value = tree.value
    if type(value) is int:
        if value >= 10:
            tree.value = None
            tree.left = Node(tree, value = math.floor(value / 2))
            tree.right = Node(tree, value = math.ceil(value / 2))
            return True
        return False

    # still tree
    split_occured = split(tree.left)
    if not split_occured:
        split_occured = split(tree.right)
    return split_occured


def magnitude(tree):
    if type(tree.value) is int:
        return tree.value

    return 3 * magnitude(tree.left) + 2 * magnitude(tree.right)


def task1():
    trees = parse_file()
    res = trees[0]

    for tree in trees[1:]:
        res = add(res, tree)
        reduce(res)
    return magnitude(res)


def task2():

    begin_time = datetime.datetime.now()

    trees = parse_file()
    max_val = float('-inf')

    for x in range(len(trees)):
        for y in range(len(trees)):

            # We modify the trees in place, so using deepcopy here to work on fresh clone
            tmp = add(parse_tree(str(trees[x])), parse_tree(str(trees[y])))
            reduce(tmp)
            value = magnitude(tmp)
            max_val = max(value, max_val)

    print(datetime.datetime.now() - begin_time)

    return max_val


print(task1())
print(task2())