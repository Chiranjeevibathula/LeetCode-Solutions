# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_subtree(inorder_start: int, postorder_start: int, subtree_size: int) -> Optional[TreeNode]:
            """
            Recursively build a subtree.
          
            Args:
                inorder_start: Starting index in the inorder array for current subtree
                postorder_start: Starting index in the postorder array for current subtree
                subtree_size: Number of nodes in the current subtree
              
            Returns:
                Root node of the subtree
            """
            # Base case: empty subtree
            if subtree_size <= 0:
                return None
          
            # The last element in postorder range is the root of current subtree
            root_val = postorder[postorder_start + subtree_size - 1]
          
            # Find root's position in inorder array
            root_inorder_idx = inorder_index_map[root_val]
          
            # Calculate size of left subtree
            left_subtree_size = root_inorder_idx - inorder_start
          
            # Recursively build left subtree
            # Left subtree elements in inorder: [inorder_start, root_inorder_idx)
            # Left subtree elements in postorder: [postorder_start, postorder_start + left_subtree_size)
            left_child = build_subtree(
                inorder_start, 
                postorder_start, 
                left_subtree_size
            )
          
            # Recursively build right subtree
            # Right subtree elements in inorder: [root_inorder_idx + 1, inorder_start + subtree_size)
            # Right subtree elements in postorder: [postorder_start + left_subtree_size, postorder_start + subtree_size - 1)
            right_child = build_subtree(
                root_inorder_idx + 1, 
                postorder_start + left_subtree_size, 
                subtree_size - left_subtree_size - 1
            )
          
            # Create and return the root node with its children
            return TreeNode(root_val, left_child, right_child)
      
        # Create a hashmap for O(1) lookup of element indices in inorder array
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
      
        # Build the entire tree starting from index 0 with all elements
        return build_subtree(0, 0, len(inorder))

        
