# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        n = len(lists)
        interval = 1
        
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]
 
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