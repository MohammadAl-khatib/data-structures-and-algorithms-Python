from stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,value):
        if not self.stack1.top :
            self.stack1.push(value)
            self.stack2.push(value)
        else:
            self.stack2 = Stack()
            self.stack1.push (value)
            current = self.stack1.top
            while current:
                self.stack2.push(current.value)
                current = current.next

    def dequeue(self):
        if self.stack2.top != None:
            return self.stack2.pop()
        else:
            return 'can not dequeue empty queue'

if __name__ == '__main__':
    psuedoqueue = PseudoQueue()
    psuedoqueue.enqueue (1)
    print (psuedoqueue.stack1.top.value)
    psuedoqueue.enqueue (2)
    print (psuedoqueue.stack1.top.value)
    psuedoqueue.enqueue (3)
    print (psuedoqueue.stack1.top.value)
    psuedoqueue.enqueue (4)
    print (psuedoqueue.stack1.top.value)


    print (psuedoqueue.dequeue())
    print (psuedoqueue.dequeue())
    print (psuedoqueue.dequeue())
    print (psuedoqueue.dequeue())


        
