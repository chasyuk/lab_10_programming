# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.getSuccessor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def getSuccessor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr
