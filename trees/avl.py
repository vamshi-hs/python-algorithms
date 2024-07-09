class Node:
    def __init__(self,data,height=0):
        self.data = data
        self.height = height
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,root,data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left,data)

        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right,data)       

    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def in_order_traversal(self,root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, end = " ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self,root):
        if root:
            print(root.data, end = " ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)


def tree_equals(x,y):
    if x is None and y is None:
        return True
    else:
        if x.data == y.data:
            # print(x.data, y.data)
            leftBool = tree_equals(x.left,y.left) 
            if leftBool:
                return tree_equals(x.right,y.right)
            else:
                return False

def test_right_rotate():
    inputTree = AVL()
    inputTree.insert(30)
    inputTree.insert(20)
    inputTree.insert(10)

    print("AVL tree preorder traversal Before: ")
    inputTree.pre_order_traversal(inputTree.root)

    inputTree.root = inputTree.right_rotate(inputTree.root)
    print()
    print("AVL tree preorder traversal After: ")
    inputTree.pre_order_traversal(inputTree.root)

    outputTree = AVL()
    outputTree.insert(20)
    outputTree.insert(10)
    outputTree.insert(30)
    
    print(tree_equals(inputTree.root,outputTree.root))

def test_tree_equals():
    tree1 = AVL()
    tree1.insert(30)
    tree1.insert(20)
    tree1.insert(10)

    tree2 = AVL()
    tree2.insert(30)
    tree2.insert(20)
    tree2.insert(10)

    print(tree_equals(tree1.root,tree2.root))

if __name__ == '__main__':
    # test_tree_equals()
    test_right_rotate()
    # avl = AVL()
    # avl.insert(10)
    # avl.insert(20)
    # avl.insert(40)
    # avl.insert(70)
    # avl.insert(50)
    #
    # print("AVL tree inorder traversal: ")
    # avl.in_order_traversal(avl.root)
    # print()
    # print("AVL tree preorder traversal: ")
    # avl.pre_order_traversal(avl.root)
