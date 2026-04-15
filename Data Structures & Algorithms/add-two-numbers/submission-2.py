# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1 
        h2 = l2
        dummy = ListNode(-1)
        temp = dummy

        carry = 0 

        while h1 and h2:
            current = h1.val + h2.val + carry 
            value = current % 10 
            carry = current // 10 
            new_node = ListNode(value)
            temp.next = new_node 
            temp = temp.next 
            h1 = h1.next 
            h2 = h2.next 

        while h1:
            current = h1.val + carry 
            value = current % 10 
            carry = current // 10 
            new_node = ListNode(value)
            temp.next = new_node 
            temp = temp.next 
            h1 = h1.next 
        
        while h2:
            current = h2.val + carry 
            value = current % 10 
            carry = current // 10 
            new_node = ListNode(value)
            temp.next = new_node 
            temp = temp.next 
            h2 = h2.next 
        
        if carry:
            temp.next = ListNode(carry)
        
        return dummy.next 











