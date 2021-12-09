from hashtable import __version__
from hashtable.hashtable import Hashtable
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_add_to_hashtable(hashtable):
    hashtable.add('Mohammad', 25)
    expected = 25
    actual = hashtable.get(("Mohammad"))
    assert expected == actual

def test_get_from_hashtable(hashtable):
    expected = 30
    actual = hashtable.get(("YAHYA"))
    assert expected == actual

def test_get_from_hashtable_none(hashtable):
    expected = None
    actual = hashtable.get(("Ibrahim"))
    assert expected == actual

def test_collision(hashtable):
    # AHMAD and HAMAD have the same hash
    expected = "{('AHMAD', 30)} -> {('HAMAD', 55)} -> None"
    actual = hashtable.map[hashtable._hash('AHMAD')].__str__()  # Finds where AHMAD is stored
    assert expected ==  actual

def test_retrive_collision(hashtable):
    expected = 55
    actual = hashtable.get(("HAMAD"))
    assert expected ==  actual

def test_hash(hashtable):
    assert hashtable._hash("HAMAD") >=0 and hashtable._hash("HAMAD") <=1024


@pytest.fixture
def hashtable():
    hashtable= Hashtable()
    hashtable.add("AHMAD",30)
    hashtable.add("YAHYA",30)
    hashtable.add("HAMAD",55)
    return hashtable