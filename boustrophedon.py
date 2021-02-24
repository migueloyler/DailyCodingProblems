'''
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isLeaf(self):
        return (self.left == None and self.right == None)

class Solution:

    def __init__(self, root):
        self.root = root
        self.arr = []

    def boustrophedon(self, root, counter):
        if counter == 0:
            self.arr.append(root.val)
        counter += 1
        if root.isLeaf():
            return
        if root.left is None:
            #doit
            self.boustrophedon(root.right, counter)
        if root.right is None:
            #doit
            self.boustrophedon(root.left, counter)
        if counter % 2 == 1:
            self.arr.append(root.right.val)
            self.arr.append(root.left.val)
            self.boustrophedon(root.left, counter)
            self.boustrophedon(root.right, counter)
        else:
            self.arr.append(root.left.val)
            self.arr.append(root.right.val)
            self.boustrophedon(root.right, counter)
            self.boustrophedon(root.left, counter)
            

d = Node(4,None,None)
e = Node(5, None, None)
f = Node(6)
g = Node(7)
b = Node(2,d,e)
c = Node(3,f,g)
a = Node(1,b,c)

solveIt = Solution(a)
solveIt.boustrophedon(solveIt.root, 0)
print(solveIt.arr)