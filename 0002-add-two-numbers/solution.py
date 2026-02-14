# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists where each node contains a single digit.
        The digits are stored in reverse order (least significant digit first).
      
        Args:
            l1: First linked list representing a number
            l2: Second linked list representing a number
          
        Returns:
            A linked list representing the sum of the two numbers
        """
        # Create a dummy head node to simplify list construction
        dummy_head = ListNode()
        carry = 0
        current_node = dummy_head
      
        # Process both lists while either has remaining digits or there's a carry
        while l1 or l2 or carry:
            # Get the current digit from each list (0 if list is exhausted)
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
          
            # Calculate sum of current digits plus any carry from previous addition
            total_sum = digit1 + digit2 + carry
          
            # Calculate new carry and the digit to store in current position
            carry, digit_value = divmod(total_sum, 10)
          
            # Create new node with the calculated digit and link it
            current_node.next = ListNode(digit_value)
            current_node = current_node.next
          
            # Move to next nodes in input lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
      
        # Return the actual result list (skip the dummy head)
        return dummy_head.next
        
