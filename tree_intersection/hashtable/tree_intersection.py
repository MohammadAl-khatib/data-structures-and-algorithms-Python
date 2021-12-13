from .hashtable2 import Hashtable
from .tree import Binary_Tree, Node


def tree_intersection(tree1, tree2):
    hashtable = Hashtable()
    tree1_repr = tree1.in_order()
    tree2_repr = tree2.in_order()

    for element in tree1_repr:
        hashtable.add(str(element), element)

    result = []
    for element in tree2_repr:
        if hashtable.contains(str(element)):
            result = result + [element]
    return result


if __name__ == '__main__':
    tree1=Binary_Tree()
    tree1.root=Node(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(4)
    tree1.root.left.right=Node(5)
    tree1.root.right.left=Node(6)

    tree2=Binary_Tree()
    tree2.root=Node(1)
    tree2.root.left=Node(2)
    tree2.root.right=Node(3)
    tree2.root.left.left=Node(4)
    tree2.root.left.right=Node(5)
    tree2.root.right.left=Node(6)

    print(tree_intersection(tree1, tree2))