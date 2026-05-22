"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Handle edge case: empty list
        if not head:
            return None
      
        # Dictionary to map original nodes to their corresponding copied nodes
        original_to_copy = {}
      
        # Create dummy node to simplify list construction
        dummy = Node(0)
        tail = dummy
      
        # First pass: create all nodes and build the next pointers
        current = head
        while current:
            # Create a new node with the same value
            new_node = Node(current.val)
          
            # Link the new node to the copied list
            tail.next = new_node
            tail = tail.next
          
            # Store mapping from original node to copied node
            original_to_copy[current] = new_node
          
            # Move to next node in original list
            current = current.next
      
        # Second pass: set up the random pointers using the mapping
        current = head
        while current:
            # Set random pointer of copied node to the copied version of the random node
            if current.random:
                original_to_copy[current].random = original_to_copy[current.random]
            else:
                original_to_copy[current].random = None
          
            # Move to next node in original list
            current = current.next
      
        # Return the head of the copied list (skip dummy node)
        return dummy.next

        
