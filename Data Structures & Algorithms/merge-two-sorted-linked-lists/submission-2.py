# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_1 = list1 
        temp_2 = list2 

        list3 = ListNode(-1)
        temp_3 = list3 

        while temp_1 and temp_2:
            if temp_1.val <= temp_2.val:
                temp_3.next = temp_1
                temp_1 = temp_1.next
                temp_3 = temp_3.next 
            else:
                temp_3.next = temp_2
                temp_2 = temp_2.next 
                temp_3 = temp_3.next 
        
        if temp_1:
            temp_3.next = temp_1

        if temp_2:
            temp_3.next = temp_2
        
        return list3.next
    