# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists):
            index = 0
            while index < len(lists) - 1:
                result = self.merge_two_lists(lists[index], lists[index+1])
                lists[index + 1] = result
                index += 1 
            
            return lists[-1]
 
    def merge_two_lists(self, list_a, list_b):
        head_1 = list_a 
        head_2 = list_b 

        head_3 = ListNode(-1)
        dummy = head_3

        while head_1 and head_2:
            if head_1.val <= head_2.val:
                dummy.next = head_1 
                head_1 = head_1.next 
                dummy = dummy.next 
            else:
                dummy.next = head_2 
                head_2 = head_2.next 
                dummy = dummy.next 
        
        if head_1:
            dummy.next = head_1
        
        if head_2:
            dummy.next = head_2 
        
        return head_3.next 