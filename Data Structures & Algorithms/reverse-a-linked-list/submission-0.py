# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        current = next = temp 

        while next:
            next = current.next 
            current.next = prev 
            prev = current 
            current = next 
        
        return prev 


        