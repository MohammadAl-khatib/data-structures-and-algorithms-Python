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
                return f"{value} is not on the linked list"

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
            return f"{value} is not on the linked list"
        
    def index_from_end(self,k):
        try:
            current = self.head
            array_linked_list = []
            while current :
                array_linked_list.append(current.value)
                current = current.next
            return array_linked_list[-(k+1)]
        except IndexError:
            return ('index not valid')

    def zip_linked_lists(ll1,ll2):
        try:
            current1 = ll1.head
            current2 = ll2.head
            if current1 == None or current2 == None:
                raise ValueError
            save_next2= current2.next
            old_next1 = None
            while current1.next:
                old_next1 = current1.next
                current1.next = current2
                current2.next = old_next1
                if save_next2 == None:
                    break
                if current1.next:
                    current1 = current1.next.next
                current2 = save_next2
                save_next2=save_next2.next
            if current1.next == None:
                current1.next = current2
        except ValueError:
            return "empty linked lists are not valid function arguments"


if __name__ == '__main__':
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll2 = LinkedList()
    ll2.insert('a')
    ll2.insert('b')
    ll2.insert('c')
    LinkedList.zip_linked_lists(ll,ll2)
