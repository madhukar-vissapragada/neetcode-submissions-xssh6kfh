# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head 

        middle = self.find_middle(head)
        second = middle.next
        middle.next = None 

        second = self.reverse_list(second)

        dummy = first
        while first and second:
            temp = first 
            first = first.next 
            temp.next = second 
            temp = temp.next
            second = second.next 
            temp.next = first 
        
    def find_middle(self, head):
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow 
    
    def reverse_list(self, head):
        prev_node = None
        curr_node = head 

        while curr_node:
            next_node = curr_node.next 
            curr_node.next = prev_node 
            prev_node = curr_node 
            curr_node = next_node 
        
        return prev_node 
    


        