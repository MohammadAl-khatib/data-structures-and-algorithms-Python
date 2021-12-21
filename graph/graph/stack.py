class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
            if not self.top:
                return None
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
 
    
    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return None
    
    def is_empty(self):
        return self.top == None
    