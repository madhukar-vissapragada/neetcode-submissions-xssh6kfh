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
        fast = head 

        

        count = 1 
        while count < n:
            fast = fast.next 
            count += 1
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next 
        
        slow.next = slow.next.next 
        return dummy_node.next 


        