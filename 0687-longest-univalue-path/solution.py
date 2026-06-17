# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_path_length=0
        def calculate_univalue_length(node:Optional[TreeNode])->int:
            if node is None:
                return 0
            left_length=calculate_univalue_length(node.left)
            right_length=calculate_univalue_length(node.right)
            left_arrow_length=left_length+1 if node.left and node.left.val==node.val else 0
            right_arrow_length=right_length+1 if node.right and node.right.val==node.val else 0
            self.max_path_length=max(self.max_path_length,left_arrow_length+right_arrow_length)
            return max(left_arrow_length,right_arrow_length)
        calculate_univalue_length(root)
        return self.max_path_length


        
