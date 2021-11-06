class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
            node = Node(value)
            if self.head == None:
                self.head = node
            else:
                current = self.head
                while current.next != None:
                    current=current.next
                current.next = node

    def includes (self,value):
        current = self.head
        while current :
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        output = ''
        current = self.head
        if current == None:
            output = f'head -> {self.head}'
        else:
            while current.next !=None:
                output += f"{{{current.value}}} -> "
                current = current.next
            output += f"{{{current.value}}} -> None"
        return output

   

def try_except(x):
    try:
        print(x/0)
    except:
        print('hello, error is working')

if __name__ == '__main__':
    try_except(1)