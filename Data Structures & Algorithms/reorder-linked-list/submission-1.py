# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle_node = self.middle(head) 
        head_1 = head 
        head_2 = middle_node.next
        middle_node.next = None
        head_2 = self.reverse(head_2)

        while head_1 and head_2:
            t1 = head_1.next
            t2 = head_2.next 

            head_1.next = head_2
            head_2.next = t1 

            head_1 = t1
            head_2 = t2 



    
    def middle(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        return slow
    

    def reverse(self, head: Optional[ListNode]):
        prev = None 
        curr = head 

        while curr:
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node 
        return prev 



        