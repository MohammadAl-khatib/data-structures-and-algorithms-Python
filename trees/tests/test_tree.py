from trees.tree import Binary_Tree, BST, Node
import pytest

def test_instantiate_empty_tree():
    tree = Binary_Tree()
    expected = None
    actual = tree.root.value
    assert expected == actual

def test_instantiate_single_node_tree():
    tree = Binary_Tree(5)
    expected = 5
    actual = tree.root.value
    assert expected == actual 

def test_add_left_to_single_node_tree():
    tree = Binary_Tree(5)
    tree.root.left = Node(10)
    expected = 10
    actual = tree.root.left.value
    assert expected == actual 

def test_add_right_to_single_node_tree():
    tree = Binary_Tree(5)
    tree.root.right = Node(10)
    expected = 10
    actual = tree.root.right.value
    assert expected == actual 

def test_pre_order(tree):
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    actual = tree.pre_order()
    assert expected == actual

def test_in_order(tree):
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    actual = tree.in_order()
    assert expected == actual

def test_post_order(tree):
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    actual = tree.post_order()
    assert expected == actual

def test_instantiate_empty_BST():
    tree = BST()
    expected = None
    actual = tree.root
    assert expected == actual

def test_add_to_empty_BST():
    tree = BST()
    tree.add(5)
    expected = 5
    actual = tree.root.value
    assert expected == actual

def test_breadth():
    tree = BST()
    tree.add(5)
    expected = [5]
    actual = tree.breadth()
    assert expected == actual

def test_add_lower_than_root_value():
    tree = BST()
    tree.add(5)
    tree.add(4)
    expected = [5,4]
    actual = tree.breadth()
    assert expected == actual

def test_add_higher_than_root_value():
    tree = BST()
    tree.add(5)
    tree.add(4)
    tree.add(10)
    expected = [5,4,10]
    actual = tree.breadth()
    assert expected == actual

def test_add_lower_than_root_two_values():
    """
    Here we try to test if values are added in the right place, pre_order was used to check, anyway in and post order can be used too
    """
    tree = BST()
    tree.add(5)
    tree.add(4)
    tree.add(10)
    tree.add(3)
    expected = [5,4,3,10]
    actual = tree.pre_order()
    assert expected == actual

def test_add_higher_than_root_two_values(bst):
    """
    Here we try to test if values are added in the right place, pre_order was used to check, anyway in and post order can be used too
    """
    expected = [5,4,3,10,13]
    actual = bst.pre_order()
    assert expected == actual

def test_contains_true(bst):
    expected = True
    actual = bst.contains(4)
    assert expected == actual

def test_contains_false(bst):
    expected = False
    actual = bst.contains(25)
    assert expected == actual

def test_contains_for_only_one_node_bst():
    bst = BST()
    bst.add(5)
    expected = True
    actual = bst.contains(5)
    assert expected == actual

def test_contains_for_empty_bst():
    bst = BST()
    expected = 'Tree is empty'
    actual = bst.contains(5)
    assert expected == actual


@pytest.fixture
def tree():
    tree = Binary_Tree('A')
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree

@pytest.fixture
def bst():
    bst = BST()
    bst.add(5)
    bst.add(4)
    bst.add(10)
    bst.add(3)
    bst.add(13)
    return bst
