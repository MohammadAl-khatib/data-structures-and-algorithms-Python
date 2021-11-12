from stack_and_queue.stack import Stack
import pytest

def test_push_first_node():
    new_stack = Stack()
    new_stack.push(5)
    expected = 5
    actual = new_stack.top.value
    assert actual == expected

def test_push_multiple_node(stack):
    # stack: 5 <- 4 <- 3 <- 2 <- top
    expected = 2
    actual =stack.top.value
    assert actual == expected

def test_pop_stack(stack):
    expected = 2
    actual = stack.pop()
    assert actual == expected

def test_pop_stack_until_empty(stack):
    # stack: 5 <- 4 <- 3 <- 2 <- top
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    expected = "Can't pop from empty stack"
    actual = stack.pop()
    assert actual == expected

def test_peek_multi_node_stack(stack):
    # stack: 5 <- 4 <- 3 <- 2 <- top
    expected = 2
    actual = stack.peek()
    assert actual == expected

def test_peek_one_node_stack():
    new_stack = Stack()
    new_stack.push('only node')
    expected = 'only node'
    actual = new_stack.peek()
    assert actual == expected

def test_instantiate_empty_stack():
    new_stack = Stack()
    expected = None
    actual = new_stack.top
    assert actual == expected

def test_is_empty_false(stack):
    # stack: 5 <- 4 <- 3 <- 2 <- top
    expected = False
    actual = stack.is_empty()
    assert actual == expected

def test_is_empty_true():
    new_stack = Stack()
    expected = True
    actual = new_stack.is_empty()
    assert actual == expected

def test_peek_empty_stack():
    new_stack = Stack()
    expected = 'stack is empty'
    actual = new_stack.peek()
    assert actual == expected

def test_pop_empty_stack():
    new_stack = Stack()
    expected = "Can't pop from empty stack"
    actual = new_stack.pop()
    assert actual == expected

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    return stack