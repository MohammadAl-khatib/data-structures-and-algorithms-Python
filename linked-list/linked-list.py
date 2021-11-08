class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        try:
            node = Node(value)
            if self.head == None:
                self.head = node
            else:
                current = self.head
                while current.next != None:
                    current=current.next
                current.next = node
        except:
            print ("hello")

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

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)

print (ll)
print({ll.head.value})
# print (ll.includes(5),ll.includes(12))


"""
ll = node1 -> node2 -> node3 -> None
"""