from insertion_sort import __version__
import insertion_sort
from insertion_sort.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'

def test_insertion_sort1():
    array =[8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertion_sort(array)
    assert expected == actual

def test_insertion_sort2():
    array =[1]
    expected = [1]
    actual = insertion_sort(array)
    assert expected == actual

def test_insertion_sort3():
    # to check that no change happens
    array =[1,2,3]
    expected = [1,2,3]
    actual = insertion_sort(array)
    assert expected == actual

def test_insertion_sort_empty():
    array =[]
    expected = []
    actual = insertion_sort(array)
    assert expected == actual

def test_insertion_sort_all_need_moving():
    # Elements are sorted in descending order in input array
    array =[5,4,3,2,1]
    expected = [1,2,3,4,5]
    actual = insertion_sort(array)
    assert expected == actual

def test_insertion_sort_strings():
    array =[1,'a','b']
    expected = 'Only numbers are allowed'
    actual = insertion_sort(array)
    assert expected == actual