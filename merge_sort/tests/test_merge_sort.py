from merge_sort import __version__
from merge_sort.merge_sort import merge_sort
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort():
    array = [8,4,23,16,15,42]
    expected = [4, 8, 15, 16, 23, 42]
    actual = merge_sort(array)
    assert expected == actual

def test_merge_sort2():
    array = [6,1,48,12]
    expected = [1,6,12,48]
    actual = merge_sort(array)
    assert expected == actual

def test_merge_sort_descending_array():
    array = [5,4,3,2,1]
    expected = [1,2,3,4,5]
    actual = merge_sort(array)
    assert expected == actual

def test_merge_sort_one_element():
    array = [1]
    expected = [1]
    actual = merge_sort(array)
    assert expected == actual

def test_merge_sort_array_containing_string():
    array = [1,14,'f',25]
    with pytest.raises (TypeError):
         merge_sort(array)