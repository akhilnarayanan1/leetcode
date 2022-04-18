# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans = self.cur = TreeNode(None)
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            
            node.left = None
            self.cur.right = node
            self.cur = node
            
            inorder(node.right)
            
    
        inorder(root)
        return ans.right