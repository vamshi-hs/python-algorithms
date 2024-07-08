class Node:
    def __init__(self,data,color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0,color="black")
        self.root = self.TNULL

    def left_rotate(self,x):
        y = x.right
        x.right = y.left

        # setting parent
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y # y is the acutal tree
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self,x):
        y = x.left
        x.left = y.right

        # setting parent
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y # y is the acutal tree
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y        

    def insert(self,key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else :
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = "black"
            return

        if node.parent.parent == None:
            return

        # self.fix_insert(node)

    def fix_insert(self,k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                uncle = k.parent.parent.left
                if uncle.color == "red":
                    uncle.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
                uncle = k.parent.parent.right
                if uncle.color == "red":
                    uncle.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break

        self.root.color = "black"
    
    def in_order_traversal(self,node):
        if node != self.TNULL:
            self.in_order_traversal(node.left)
            print(node.data)
            self.in_order_traversal(node.right)


    def print_tree(self):
        self.in_order_traversal(self.root)
        print()

if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(15)
    bst.insert(25)
    bst.insert(5)
    
    print("inorder traversal: ",end="")
    bst.print_tree()
