class Node:
    def __init__(self,data,height=1):
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
            return
        
        self._insert(self.root,data)
        self.root.height = self.update_height(self.root)
        self.root = self.make_balance(self.root)

    def get_balance(self,root):
        if root is not None:
            leftHeight = root.left.height if root.left else 0
            rightHeight = root.right.height if root.right else 0
            return leftHeight - rightHeight
        return 0

    def update_height(self,root):
        if root is None:
            return 0
        else:
            leftHeight = root.left.height if root.left is not None else 0
            rightHeight = root.right.height if root.right is not None else 0
            treeHeight = leftHeight if leftHeight > rightHeight else rightHeight
            return 1 + treeHeight 

    def make_balance(self,root):
        if self.get_balance(root) <= -2:
            if self.get_balance(root.right) == 1:
                root.right = self.right_rotate(root.right)
            root = self.left_rotate(root)
                
        if self.get_balance(root) >= 2:
            if self.get_balance(root.left) == -1:
                root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
            
        return root

    def _insert(self,root,data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left,data)
                root.left.height = self.update_height(root.left)
                root.left = self.make_balance(root.left)

        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right,data)
                root.right.height = self.update_height(root.right)
                root.right = self.make_balance(root.right)

    def right_rotate(self,x):
        if x is not None and x.left is not None:
            y = x.left
            x.left = y.right
            y.right = x
            x.height = self.update_height(x)
            y.height = self.update_height(y)
            return y
        else:
            return x

    def left_rotate(self,x):
        if x is not None and x.right is not None:
            y = x.right
            x.right = y.left
            y.left = x
            x.height = self.update_height(x)
            y.height = self.update_height(y)
            return y
        else:
            return x

    def in_order_traversal(self,root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, "height: ", root.height, end = " ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self,root):
        if root:
            print("d:", root.data, "h:", root.height)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

def tree_equals(x,y):
    if x is None and y is None:
        return True
    else:
        if x.data == y.data:
            leftBool = tree_equals(x.left,y.left) 
            if leftBool:
                return tree_equals(x.right,y.right)
            else:
                return False
        else:
            return False

def test_left_rotate():
    inputTree = AVL()
    inputTree.insert(10)
    inputTree.insert(20)
    inputTree.insert(30)

    print("AVL tree preorder traversal Before: ")
    inputTree.pre_order_traversal(inputTree.root)

    inputTree.root = inputTree.left_rotate(inputTree.root)
    print()
    print("AVL tree preorder traversal After: ")
    inputTree.pre_order_traversal(inputTree.root)

    outputTree = AVL()
    outputTree.insert(20)
    outputTree.insert(10)
    outputTree.insert(30)

    print()
    print("Test equal?",tree_equals(inputTree.root,outputTree.root))

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

def new_insert_test():
    tree1 = AVL()
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    tree1.insert(40)
    tree1.insert(50)

    print("AVL tree preorder traversal Before: ")
    tree1.pre_order_traversal(tree1.root)

    print("AVL tree inorder traversal Before: ")
    tree1.in_order_traversal(tree1.root)
    
if __name__ == '__main__':
    # test_tree_equals()
    # test_right_rotate()
    # test_left_rotate()
    new_insert_test()
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
