from trees.queue import Queue

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root = None):
        self.root = Node(root)

    def pre_order(self):
        output = []
        def _traverse(root = self.root):
            output.append(root.value)
            if root.left :
                _traverse(root.left)
            if root.right :
                _traverse(root.right)
        _traverse()
        return output

    def in_order(self):
        output = []
        def _traverse(root = self.root):
            if root.left :
                _traverse(root.left)
            output.append(root.value)
            if root.right :
                _traverse(root.right)
        _traverse()
        return output

    def post_order(self):
        output = []
        def _traverse(root = self.root):
            if root.left :
                _traverse(root.left)
            if root.right :
                _traverse(root.right)
            output.append(root.value)
        _traverse()
        return output

class BST(Binary_Tree):
    def __init__(self):
        self.root = None

    def breadth(self):
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
    
    def add(self,value):

        if not self.root : 
            self.root = Node(value)
            return

        queue = Queue()
        queue.enqueue(self.root)

        while queue.peek():
            node = queue.dequeue()
            if node.value > value:
                if node.left:
                    queue.enqueue(node.left)
                if not node.left:
                    node.left = Node(value)
                    break
                
            else: 
                if node.right:
                    queue.enqueue(node.right)
                if not node.right:
                    node.right = Node(value)
                    break

    def contains(self,value):
        if not self.root : 
            return 'Tree is empty'

        queue = Queue()
        queue.enqueue(self.root)

        while queue.peek():
            node = queue.dequeue()
            if node.value == value : return True
            if node.value > value:
                if node.left:
                    if node.left.value == value : return True
                    queue.enqueue(node.left)
              
            else: 
                if node.right:
                    if node.right.value == value : return True
                    queue.enqueue(node.right)
        return False
        

        
        

tree=Binary_Tree()
tree.root=Node("A")
tree.root.left=Node("B")
tree.root.right=Node("C")
tree.root.left.left=Node("D")
tree.root.left.right=Node("E")
tree.root.right.left=Node("F")

bst = BST()
bst.add(23)
bst.add(8)
bst.add(42)
bst.add(4)
bst.add(16)
bst.add(27)
bst.add(85)
bst.add(15)

new_bst = BST()
new_bst.add(20)


print (bst.pre_order())
print  (new_bst.contains(20))

print (tree.pre_order())
print (tree.in_order())
print (tree.post_order())
