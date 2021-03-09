class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        # print(self.value, target)
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    def printTree(self):
        if self is not None:
            if self.left is not None:
                self.left.printTree()

            print(self.value)

            if self.right is not None:
                self.right.printTree()

class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, target):
        return self.root.search(target)

    def printTree(self):
        self.root.printTree()

binarySearchTree = BST(25)

binarySearchTree.insert(15)
binarySearchTree.insert(50)

binarySearchTree.insert(10)
binarySearchTree.insert(22)

binarySearchTree.insert(35)
binarySearchTree.insert(70)

binarySearchTree.printTree()