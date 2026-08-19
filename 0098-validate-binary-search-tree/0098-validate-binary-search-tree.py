# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node:Optional[TreeNode])->bool:
            if node is None:
                return True
            if not inorder_traversal(node.left):
                return False
            nonlocal previous_value
            if previous_value>=node.val:
                return False
            previous_value=node.val
            return inorder_traversal(node.right) 
        previous_value=-inf
        return inorder_traversal(root)               

        