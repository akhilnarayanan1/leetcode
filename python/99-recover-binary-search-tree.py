# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Create a list through inorder traversal
        wrong_list = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            wrong_list.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        # Get linear time swapped numbers
        def find_two_swapped(nums: List[int]) -> (int, int):
            n = len(nums)
            x = y = None # Initialize x and y as a value that cannot be the value of a node.
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:     
                        x = nums[i]
                    else:           
                        break
            return x, y
        
        x, y = find_two_swapped(wrong_list)
        
        # Replace the values using Inorder again
        def replace_inorder(node):
            if node is None:
                return
            replace_inorder(node.left)
            
            node.val = y if node.val==x else x if node.val==y else node.val
            
            replace_inorder(node.right)
            
        replace_inorder(root)
        
        return root