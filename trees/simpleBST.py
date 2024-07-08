class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)

    def _insert(self,root,key):
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left,key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right,key)

    def search(self,key):
        return self._search(self.root,key)

    def _search(self,root,key):
        if root.data == key:
            return True
        elif key < root.data:
            return self._search(root.left,key)
        else:
            return self._search(root.right,key)


    def in_order_traversal(self,root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, end = " ")
            self.in_order_traversal(root.right)

    def delete(self,key):
        self.root = self._delete(self.root,key)

    def _delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self._delete(root.left,key)
        elif key > root.data:
            root.right = self._delete(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right,root.data)

    def _min_value_node(self,node):
        current = node
        while current.left is not None:
           current = current.left
        return current

if __name__ == "__main__":
    bst = BST()

    bst.insert(10)
    bst.insert(20)
    bst.insert(15)
    bst.insert(35)
    bst.insert(-5)

    print("Inorder traversal: ")
    bst.in_order_traversal(bst.root)
