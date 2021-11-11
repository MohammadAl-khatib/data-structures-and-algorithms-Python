from stack_and_queue.node import Node

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
        try:
            if not self.top:
                raise Exception
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except:
            return "Can't pop from empty stack"
    
    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return 'stack is empty'
    
    def is_empty(self):
        return self.top == None
    