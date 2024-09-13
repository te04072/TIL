# 최대힙
# def enq(n):
#     global last
#     last += 1
#     h[last] = n
#     c = last
#     p = c//2
#     while p >= 1 and h[p] < h[c]:
#         h[p], h[c] = h[c], h[p]
#         c = p
#         p = c//2
#
#
# def deq():
#     global last
#     tmp = h[1]
#     h[1] = h[last]
#     last -= 1
#     p = 1
#     c = p*2
#     while c <= last:
#         if c+1 <= last and h[c] < h[c+1]:
#             c += 1
#         if h[p] < h[c]:
#             h[p], h[c] = h[c], h[p]
#             p = c
#             c = p*2
#         else:
#             break
#     return tmp
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# h = [0]*(N+1)
# last = 0
#
# for num in arr:
#     enq(num)
#     print(h)
#
# print(h)
# while last > 0:
#     print(deq(), end=' ')


# BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)
N = int(input())
arr = list(map(int, input().split()))
bst = BinarySearchTree()
for num in arr:
    bst.insert(num)
bst.inorder_traversal()

key = 5
result = bst.search(key)
if result:
    print(f"{key} found")
else:
    print(f"{key} not found")