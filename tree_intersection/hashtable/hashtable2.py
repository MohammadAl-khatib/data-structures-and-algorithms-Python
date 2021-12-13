from .linked_list import LinkedList
import re

class Hashtable():
    def __init__(self, size = 1024):
        self.size = size           # defined in case we want to change the size
        self.map = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        sum_ascii = 0
        for char in key:
            sum_ascii += ord(char)
        sum_ascii_times_primary = sum_ascii * 599
        hash = sum_ascii_times_primary%self.size
        return hash
    
    def add(self, key, value):
        hashed_key = self._hash(key)
        self.map[hashed_key].insert((key, value))

    def get(self, key):
        hashed_key = self._hash(key)
        current = self.map[hashed_key].head     # To find the element in hashtable and store the head of it 
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        else:
            return self.map[hashed_key].head
    
    def contains(self, key):
        hashed_key = self._hash(key)
        current = self.map[hashed_key].head     # To find the element in hashtable and store the head of it 
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        else:
            return False

            
def repeated_word(text):
    store_text = Hashtable()
    
    for char in text.split(' '):            
        if store_text.contains(char):
            return char
        store_text.add(char.split(',')[0].lower(), char.lower())
        
    return 'No repeated word'

