# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.solve(head, None)
        return self.head  
    
    def solve(self, current, prev):
        if current == None:
            self.head = prev 
            return 
        
        self.solve(current.next, current)
        current.next = prev 


        