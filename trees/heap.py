class MinHeap():
    def __init__(self):
        self.heap = []

    def insert(self,key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._bubble_down(0)

        return root

    def _bubble_up(self,index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self,index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] <  self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] <  self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def get_min(self):
        if self.heap :
            return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class MaxHeap():
    def __init__(self):
        self.heap = []

    def insert(self,key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._bubble_down(0)

        return root

    def _bubble_up(self,index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self,index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def get_max(self):
        if self.heap :
            return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

def minTest():
    minTree = MinHeap()
    minTree.insert(40)
    minTree.insert(60)
    minTree.insert(70)
    minTree.insert(20)
    minTree.insert(50)
    minTree.insert(30)
    minTree.insert(10)

    print("Before extracting min: ",minTree.heap)
    print("Extracting min..... ")
    minValue = minTree.extract_min()
    print("Min value",minValue)
    print("After extracting min: ",minTree.heap)

def maxTest():
    maxTree = MaxHeap()
    maxTree.insert(40)
    maxTree.insert(60)
    maxTree.insert(70)
    maxTree.insert(20)
    maxTree.insert(50)
    maxTree.insert(30)
    maxTree.insert(10)

    print("Before extracting max: ",maxTree.heap)
    print("Extracting max..... ")
    maxValue = maxTree.extract_max()
    print("Max value",maxValue)
    print("After extracting max: ",maxTree.heap)

if __name__ == '__main__':
    maxTest()
