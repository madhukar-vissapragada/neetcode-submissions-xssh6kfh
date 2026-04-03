# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged_list = None
        dummy_node = ListNode(-1)
        merged_list_head = dummy_node

        temp_1 = list1
        temp_2 = list2

        while temp_1 and temp_2:
            if temp_1.val <= temp_2.val:
                new_node = ListNode(temp_1.val)
                dummy_node.next = new_node
                dummy_node = new_node
                temp_1 = temp_1.next
            else:
                new_node = ListNode(temp_2.val)
                dummy_node.next = new_node
                dummy_node = new_node
                temp_2 = temp_2.next

        while temp_1:
            new_node = ListNode(temp_1.val)
            dummy_node.next = new_node
            dummy_node = new_node
            temp_1 = temp_1.next

        while temp_2:
            new_node = ListNode(temp_2.val)
            dummy_node.next = new_node
            dummy_node = new_node
            temp_2 = temp_2.next

        merged_list_head = merged_list_head.next

        return merged_list_head
