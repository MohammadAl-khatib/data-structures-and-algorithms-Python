import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_init ():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

def test_insert ():
    ll = LinkedList()
    ll.insert(1)
    expected = 1
    actual = ll.head.value
    assert expected == actual

def test_head(ll):
    expected = 1
    actual = ll.head.value
    assert expected == actual

def test_multiple_insert(ll):
    current = ll.head
    expected = 1
    while current:
        actual= current.value
        assert expected == actual
        current = current.next
        expected +=1

def test_includes_true(ll):
    expected = True
    actual = ll.includes(1)
    assert expected == actual

def test_includes_false(ll):
    expected = False
    actual = ll.includes(4)
    assert expected == actual

def test_return_all_linked_list(ll):
    expected = '{1} -> {2} -> {3} -> None'
    actual = ll.__str__()
    assert expected == actual

@pytest.fixture
def ll():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll