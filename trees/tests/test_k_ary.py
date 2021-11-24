from trees.k_ary import Node, K_ary, fizz_buzz_tree
import pytest

def test_fizz_buzz_tree1(tree):
    expected = ['Buzz', 'Fizz', '2', 'FizzBuzz', 'FizzBuzz', '14']
    actual = fizz_buzz_tree(tree).breadth()
    assert actual == expected

def test_fizz_buzz_tree2(tree):
    tree.root.childs[1].childs.append(Node(40))
    expected = ['Buzz', 'Fizz', '2', 'FizzBuzz', 'FizzBuzz', 'Buzz', '14']
    actual = fizz_buzz_tree(tree).breadth()
    assert actual == expected

def test_fizz_buzz_tree3(tree):
    tree.root.childs[2].childs.append(Node(37))
    expected = ['Buzz', 'Fizz', '2', 'FizzBuzz', 'FizzBuzz', '37', '14']
    actual = fizz_buzz_tree(tree).breadth()
    assert actual == expected

def test_empty_tree():
    tree = K_ary()
    expected = 'Tree is empty'
    actual = fizz_buzz_tree(tree)
    assert expected == actual

def test_one_node_tree():
    tree = K_ary(5)
    expected = ['Buzz']
    actual = fizz_buzz_tree(tree).breadth()
    assert expected == actual

@pytest.fixture
def tree():
    tree = K_ary(5)
    tree.root.childs.append(Node(3))
    tree.root.childs[0].childs.append(Node(30))
    tree.root.childs[0].childs[0].childs.append(Node(14))
    tree.root.childs.append(Node(2))
    tree.root.childs.append(Node(15))
    return tree