# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head

        
        slow = dummy_node
        fast = dummy_node 

        counter = 0

        while counter < n:
            counter += 1 
            fast = fast.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next 
        
        node_to_delete = slow.next 
        slow.next = node_to_delete.next 

        return dummy_node.next 
        