import pytest
from stack_and_queue.queue import Queue

def test_enqueue_one_value():
    new_queue = Queue()
    new_queue.enqueue ('a')
    expected = 'a'
    actual = new_queue.rear.value
    assert actual == expected

def test_enqueue_multiple_values(new_queue):
    expected = 'front -> a -> b -> c -> d -> f <- rear'
    actual = new_queue.__str__()
    assert actual == expected

def test_dequeue(new_queue):
    expected = 'a'
    actual = new_queue.dequeue()
    assert actual == expected

def test_peek(new_queue):
    expected = 'a'
    actual = new_queue.peek()
    assert actual == expected

def test_dequeue_until_empty(new_queue):
    while new_queue.front:
        new_queue.dequeue()
    expected = 'front -> None <- rear'
    actual = new_queue.__str__()
    assert actual == expected

def  test_instantiate_empty_queue():
    queue = Queue()
    expected = 'front -> None <- rear'
    actual = queue.__str__()
    assert actual == expected

def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises (AttributeError):
        queue.peek()

def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises (AttributeError):
        queue.dequeue()

def test_front_equals_rear_one_node_queue():
    queue = Queue()
    queue.enqueue(1)
    expected = True
    actual = queue.front == queue.rear
    assert actual == expected

@pytest.fixture
def new_queue():
    new_queue = Queue()
    new_queue.enqueue ('a')
    new_queue.enqueue ('b')
    new_queue.enqueue ('c')
    new_queue.enqueue ('d')
    new_queue.enqueue ('f')
    return new_queue
