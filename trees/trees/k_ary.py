from trees.queue import Queue

class Node:
    def __init__(self, value = None):
        self.value = value
        self.childs = []

class K_ary:

    def __init__(self, root = None):
        self.root = Node(root)

    def breadth(self):
        if not self.root.value:
            return 'Tree is empty'
        queue = Queue()
        output = []
        queue.enqueue(self.root)

        while queue.peek():
            node = queue.dequeue()
            if node.value %3 == 0 and node.value%5 ==0:
                output.append('FizzBuzz')
            elif node.value %3 == 0:
                output.append('Fizz')
            elif node.value %5 == 0:
                output.append('Buzz')
            else:
                output.append(str(node.value))
            for child in node.childs:
                queue.enqueue(child)

        return output



tree = K_ary(5)
tree.root.childs.append(Node(3))
tree.root.childs.append(Node(2))
tree.root.childs.append(Node(15))
print (tree.breadth())


def breadth(self):
        if not self.root.value:
            return 'Tree is empty'
        queue = Queue()
        output = []
        queue.enqueue(self.root)

        while queue.peek():
            node = queue.dequeue()
            output.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return output