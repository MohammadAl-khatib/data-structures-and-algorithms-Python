from stack_and_queue.pseudo_queue import PseudoQueue
import pytest

def test_enqueue():
     psuedoqueue = PseudoQueue()
     psuedoqueue.enqueue (1)
     psuedoqueue.enqueue (2)
     psuedoqueue.enqueue (3)
     psuedoqueue.enqueue (4)
     expected = 4
     actual = psuedoqueue.stack1.top.value
     assert expected == actual

def test_dequeue():
     psuedoqueue = PseudoQueue()
     psuedoqueue.enqueue (1)
     psuedoqueue.enqueue (2)
     psuedoqueue.enqueue (3)
     psuedoqueue.enqueue (4)
     expected = 1
     actual = psuedoqueue.dequeue()
     assert expected == actual

def test_enqueue_one_value():
     psuedoqueue = PseudoQueue()
     psuedoqueue.enqueue (1)
     expected = 1
     actual = psuedoqueue.stack1.top.value
     assert expected == actual

def test_dequeue_one_value():
     psuedoqueue = PseudoQueue()
     psuedoqueue.enqueue (1)
     expected = 1
     actual = psuedoqueue.dequeue()
     assert expected == actual

def test_dequeue_empty_queue():
     psuedoqueue = PseudoQueue()
     expected = 'can not dequeue empty queue'
     actual = psuedoqueue.dequeue()
     assert expected == actual
