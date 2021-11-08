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

def test_insert_before_first(ll):
    ll.insert_before(1,'before first')
    expected = '{before first} -> {1} -> {2} -> {3} -> None'
    actual = ll.__str__()
    assert expected == actual

def test_insert_before_mid(ll):
    ll.insert_before(3,'before mid')
    expected = '{1} -> {2} -> {before mid} -> {3} -> None'
    actual = ll.__str__()
    assert expected == actual

def test_insert_after_mid(ll):
    ll.insert_after(3,"after mid")
    expected = '{1} -> {2} -> {3} -> {after mid} -> None'
    actual = ll.__str__()
    assert expected == actual

def test_insert_after_last(ll):
    ll.insert_after(3,"after last")
    expected = '{1} -> {2} -> {3} -> {after last} -> None'
    actual = ll.__str__()
    assert expected == actual

def test_insert_before_value_not_in_list(ll):
    expected = '6 is not on the linked list'
    actual = ll.insert_before(6,'any value')
    assert expected == actual

def test_insert_after_value_not_in_list(ll):
    expected = '8 is not on the linked list'
    actual = ll.insert_after(8,'any value')
    assert expected == actual

def test_index_from_end_bigger_than_length(ll):
    expected = 'index not valid'
    actual = ll.index_from_end(4)
    assert expected == actual 

def test_index_from_end_equal_to_length(ll):
    expected = 'index not valid'
    actual = ll.index_from_end(3)
    assert expected == actual 

def test_index_from_end_negative(ll):
    expected = 1
    actual = ll.index_from_end(-1)
    assert expected == actual 

def test_index_from_end_middle1(ll):
    expected = 2
    actual = ll.index_from_end(1)
    assert expected == actual 

def test_index_from_end_single_value_ll():
    ll = LinkedList()
    ll.insert(1)
    expected = 1
    actual = ll.index_from_end(0)
    assert expected == actual 
    
@pytest.fixture
def ll():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll