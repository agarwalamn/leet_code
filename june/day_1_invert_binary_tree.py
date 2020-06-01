# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root:TreeNode):
        if root:
            
            temp=self.traverse(root.left)
            root.left=self.traverse(root.right)
            root.right=temp
            return root
            
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        self.traverse(root)
        return root
    
