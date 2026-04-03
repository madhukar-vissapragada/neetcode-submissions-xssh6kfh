# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.solve(None, head)
        return self.head
    
    def solve(self, prev, curr):
        if curr is None:
            self.head = prev 
            return 
        
        self.solve(curr, curr.next)
        curr.next = prev 
    

        