import pytest
from stack_and_queue.animal_shelter import AnimalShelter

def test_enqueue_cat():
    animals = AnimalShelter()
    animals.enqueue('cat', 'lilly')
    expected = 'lilly'
    actual = animals.cats.front.value
    assert expected == actual

def test_enqueue_dog():
    animals = AnimalShelter()
    animals.enqueue('dog', 'potchy')
    expected = 'potchy'
    actual = animals.dogs.front.value
    assert expected == actual

def test_dequeue_dog():
    animals = AnimalShelter()
    animals.enqueue('dog', 'potchy')
    expected = 'potchy'
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_cat():
    animals = AnimalShelter()
    animals.enqueue('cat', 'lilly')
    expected = 'lilly'
    actual = animals.dequeue('cat')
    assert expected == actual

def test_enqueue_multiple1():
    animals = AnimalShelter()
    animals.enqueue('dog', 'potchy')
    animals.enqueue('cat', 'lilly')
    animals.enqueue('dog', 'harold')
    animals.enqueue('cat', 'meaw')
    expected = 'lilly'
    actual = animals.cats.front.value
    assert expected == actual

def test_enqueue_multiple2():
    animals = AnimalShelter()
    animals.enqueue('dog', 'potchy')
    animals.enqueue('cat', 'lilly')
    animals.enqueue('dog', 'harold')
    animals.enqueue('cat', 'meaw')
    expected = 'potchy'
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_cat_empty():
    animals = AnimalShelter()
    expected = None
    actual = animals.dequeue('cat')
    assert expected == actual

def test_dequeue_dog_empty():
    animals = AnimalShelter()
    expected = None
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_neighther_dog_or_cat_empty():
    animals = AnimalShelter()
    animals.enqueue('dog', 'potchy')
    expected = None
    actual = animals.dequeue('horse')
    assert expected == actual


