import fileinput
import math

class Node:
    def __init__(self, parent, value = None, left = None, right = None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value and self.right == other.right and self.left == other.left


    def __str__(self):
        if self.left is None and self.right is None:
        # if type(self.value) is int:
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
    example = parse_tree('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')

    any_action = True

    while any_action:
        exploded = True
        while exploded:
            exploded = explode(tree)
            if exploded:
                print('after explode', tree)


        splitted = split(tree)
        if splitted:
            print('after split', tree)
            print('tree == example', tree == example)

        any_action = exploded or splitted

def explode(tree, level = 0):
    # print(tree)
    if tree is None or (type(tree.value) is int and level < 4):
        return False

    if level == 4 and tree.left is not None and tree.right is not None:
        assert type(tree.left.value) is int
        assert type(tree.right.value) is int
        # print('level=4', tree)
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
        print('left subtree', left_subtree)
        rightmost = find_rightmost_leaf(left_subtree)
        print('rightmost', rightmost, value)
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
    print('right subtree', right_subtree)
    if right_subtree:
        print('right_subtree', right_subtree)
        leftmost = find_leftmost_leaf(right_subtree)
        print('leftmost', leftmost, value)
        if leftmost:
            leftmost.value += value


def find_right_subtree(tree):
    print('looking for right subtree', tree)
    parent = tree.parent
    print('parent', parent)
    # root
    if parent.parent is None:
        print('parent.parent is None')
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

example = parse_tree('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')

print(example)
reduce(example)
print(example)
print('')



def task1():
    trees = parse_file()
    res = trees[0]

    for tree in trees[1:]:
        print(res)
        res = add(res, tree)
        print('after addition: ', res)
        reduce(res)
    print(res)
    return magnitude(res)

print(task1())