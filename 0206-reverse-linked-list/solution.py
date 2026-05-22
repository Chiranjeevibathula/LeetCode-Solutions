# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode()
        current=head
        while current:
            next_node=current.next
            current.next=dummy_node.next
            dummy_node.next=current
            current=next_node
        return dummy_node.next    

        
