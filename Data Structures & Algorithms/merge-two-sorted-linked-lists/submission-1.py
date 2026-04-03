# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode(-1)
        temp = merged_list

        temp_1 = list1
        temp_2 = list2 

        while temp_1 and temp_2:
            if temp_1.val <= temp_2.val:
                temp.next = temp_1
                temp_1 = temp_1.next
            else:
                temp.next = temp_2 
                temp_2 = temp_2.next 
            temp = temp.next 
        
        if temp_1:
            temp.next = temp_1
        
        if temp_2:
            temp.next = temp_2 
        
        return merged_list.next

            

