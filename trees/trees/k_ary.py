from trees.queue import Queue
import copy

class Node:
    def __init__(self, value = None):
        self.value = value
        self.childs = []

class K_ary:

    def __init__(self, root = None):
        self.root = Node(root)
    
    def breadth(self):
        '''
        This method is used to return a list representing the tree in breadth approach
        '''
        if not self.root.value:
            return 'Tree is empty'
        queue = Queue()
        output = []
        queue.enqueue(self.root)

        while queue.peek():
            node = queue.dequeue()
            output.append(node.value)
            for child in node.childs:
                queue.enqueue(child)

        return output


def fizz_buzz_tree(tree):

        if not tree.root.value:
            return 'Tree is empty'
        result = copy.deepcopy(tree)
        queue = Queue()
        queue.enqueue(result.root)
        
        while queue.peek():
            node = queue.dequeue()
            if node.value %3 == 0 and node.value %5 ==0:
                node.value ='FizzBuzz'
            elif node.value %3 == 0:
                node.value ='Fizz'
            elif node.value %5 == 0:
                node.value ='Buzz'
            else:
                node.value = str(node.value)
            for child in node.childs:
                queue.enqueue(child)

        return result



tree = K_ary(5)
tree.root.childs.append(Node(3))
tree.root.childs[0].childs.append(Node(30))
tree.root.childs[0].childs[0].childs.append(Node(14))
tree.root.childs.append(Node(2))
tree.root.childs.append(Node(15))

print (fizz_buzz_tree(tree).breadth())
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