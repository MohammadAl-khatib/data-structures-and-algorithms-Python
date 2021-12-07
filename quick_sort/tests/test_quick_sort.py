from quick_sort import __version__
from quick_sort.quick_sort import QuickSort
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_quick_sort():
    array = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual

def test_quick_sort2():
    array = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual

def test_quick_sort3():
    array = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual
    
def test_quick_sort4():
    array = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual

def test_quick_sort_one_element():
    array = [2]
    expected = [2]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual

def test_quick_sort_ascending_ordered_array():
    array = [6,5,4,3,2,1]
    expected = [1,2,3,4,5,6]
    actual = QuickSort (array, 0, len(array)-1)
    assert expected == actual

def test_quick_sort_array_with_strings():
    array = [6,5,4,'k',2,1]
    with pytest.raises (TypeError):
        QuickSort (array, 0, len(array)-1)
