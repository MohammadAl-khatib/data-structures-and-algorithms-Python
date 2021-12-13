from hashtable.tree_intersection import tree_intersection
from hashtable.tree import Binary_Tree, Node
import pytest

def test_tree_intersection(tree1, tree2):
    expected = [4, 2, 5, 1, 6, 3]
    actual = tree_intersection(tree1, tree2)
    assert expected == actual

def test_tree_intersection2(tree1, tree3):
    expected = [6, 2, 1, 3]
    actual = tree_intersection(tree1, tree3)
    assert expected == actual

def test_tree_intersection3(tree2, tree3):
    expected = [6, 2, 1, 3]
    actual = tree_intersection(tree2, tree3)
    assert expected == actual

def test_tree_intersection4(tree5, tree6):
    expected = ['b', 'a', 'c']
    actual = tree_intersection(tree5, tree6)
    assert expected == actual

def test_tree_intersection_no_match(tree1, tree4):
    expected = []
    actual = tree_intersection(tree1, tree4)
    assert expected == actual

def test_tree_intersection_empty_tree(tree1):
    tree = Binary_Tree()
    expected = []
    actual = tree_intersection(tree1, tree)
    assert expected == actual
    

@pytest.fixture
def tree1():
    tree1=Binary_Tree()
    tree1.root=Node(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(4)
    tree1.root.left.right=Node(5)
    tree1.root.right.left=Node(6)
    return tree1

@pytest.fixture  
def tree2():
    tree2=Binary_Tree()
    tree2.root=Node(1)
    tree2.root.left=Node(2)
    tree2.root.right=Node(3)
    tree2.root.left.left=Node(4)
    tree2.root.left.right=Node(5)
    tree2.root.right.left=Node(6)
    return tree2

@pytest.fixture
def tree3():
    tree3=Binary_Tree()
    tree3.root=Node(1)
    tree3.root.left=Node(2)
    tree3.root.right=Node(3)
    tree3.root.left.left=Node(6)
    tree3.root.left.right=Node(7)
    tree3.root.right.left=Node(8)
    return tree3

@pytest.fixture
def tree4():
    tree4=Binary_Tree()
    tree4.root=Node(0)
    tree4.root.left=Node(0)
    tree4.root.right=Node(0)
    tree4.root.left.left=Node(0)
    tree4.root.left.right=Node(0)
    tree4.root.right.left=Node(0)
    return tree4

@pytest.fixture
def tree5():
    tree5=Binary_Tree()
    tree5.root=Node('a')
    tree5.root.left=Node('b')
    tree5.root.right=Node('c')
    tree5.root.left.left=Node('g')
    tree5.root.left.right=Node('k')
    tree5.root.right.left=Node('l')
    return tree5

@pytest.fixture
def tree6():
    tree6=Binary_Tree()
    tree6.root=Node('a')
    tree6.root.left=Node('b')
    tree6.root.right=Node('c')
    tree6.root.left.left=Node('m')
    tree6.root.left.right=Node('n')
    tree6.root.right.left=Node('y')
    return tree6

    