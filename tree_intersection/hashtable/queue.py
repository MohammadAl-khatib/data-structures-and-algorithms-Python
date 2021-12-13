class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        current = self.front
        output = ''
        while current:
            if current.next == None:
                output += f'{current.value}'
            else:
                output += f'{current.value} -> '
            current = current.next
        return f'front -> {output or None} <- rear'


    def enqueue(self,value):
        node = Node (value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError

    def peek(self):
        if self.front:
            return self.front.value
        return  None

    def is_empty(self):
        return self.front == None

if __name__ == '__main__':
    new_queue = Queue()
    new_queue.enqueue ('a')
    new_queue.enqueue ('b')
    new_queue.enqueue ('c')
    new_queue.enqueue ('d')
    print (new_queue)

