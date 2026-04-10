# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.solve(None, head)
        return self.head

    def solve(self, prev_node, curr_node):
        if curr_node is None:
            self.head = prev_node 
            return 
        
        self.solve(curr_node, curr_node.next)
        curr_node.next = prev_node
        