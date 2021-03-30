'''
Invert a binary tree.
'''

def inverBinary(root):
  if root.left == None and root.right == None:
    return
  tmp = root.left
  root.left = root.right
  root.right = tmp
  invertBinary(root.left)
  invertBinary(root.right)
  return
