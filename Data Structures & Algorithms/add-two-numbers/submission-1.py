# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        temp = dummy_node 
        carry = 0 

        while l1 or l2 or carry:
            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0 
            current_sum = a + b + carry 
            new_node = ListNode(current_sum % 10)
            carry = current_sum // 10 
            temp.next = new_node 
            temp = new_node 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 

        return dummy_node.next  