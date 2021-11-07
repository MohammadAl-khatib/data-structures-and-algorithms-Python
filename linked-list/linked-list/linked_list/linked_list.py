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

    def insert_before(self,value,new_value):
        current = self.head
        if current.value == value:
            new_node = Node (new_value)
            new_node.next = current
            self.head = new_node
        else:
            while current.next:
                if current.next.value == value:
                    new_node = Node (new_value)
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
        if current.next == None:
                print (f"{value} is not on the linked list")

    def insert_after(self,value,new_value):
        current = self.head
        while current :
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
        if current == None:
                return (f"{value} is not on the linked list")
        

if __name__ == '__main__':
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    # ll.insert(4)
    # ll.insert(5)
    # ll.insert_before(1,'before first')
    # ll.insert_before(3,'before mid')
    # ll.insert_after(3,"after mid")
    # ll.insert_after(3,'after last')
    # ll.insert_before(6,'value')
    # ll.insert_after(6,'value')
    print(ll)