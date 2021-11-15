from stack_and_queue.queue import Queue

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self,type, name):
        if type == 'cat':
            self.cats.enqueue(name)
        if type == 'dog':
            self.dogs.enqueue(name)
            
    def dequeue(self,pref):
        try:
            if pref == 'cat':
                return self.cats.dequeue()
            if pref == 'dog':
                return self.dogs.dequeue()
        except:
            return None

if __name__ == '__main__':
    pass