# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head 
        
        current = self.validate(head, k)
        if current is None:
            return head 
        
        temp_node = current.next 
        current.next = None 
        reversed_list = self.reverse_list(head)
        head.next = self.reverseKGroup(temp_node, k)
        return reversed_list
            
    def reverse_list(self, head: Optional[ListNode]):
        prev_node = None 
        curr_node = head 

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = next_node 
        
        return prev_node 
    

    def validate(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head 
        current_length = 1 

        while temp and current_length != k:
            temp = temp.next 
            current_length += 1 
        
        return temp 

    

        