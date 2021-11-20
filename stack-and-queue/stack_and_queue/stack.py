from node import Node

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

def get_max(stack):
    if stack.top == None : return 'stack is empty'
    max = stack.top.value
    current = stack.top
    while current:
        if current.value > max:
            max = current.value
        current = current.next
    return max

stack  = Stack()
# stack.push(1)
# stack.push(20)
# stack.push(-10)
# stack.push(13)
# stack.push(4)

print (get_max(stack))

    