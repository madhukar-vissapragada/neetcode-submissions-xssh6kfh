# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. create a dummy_node and attach it to the linked list
        dummy_node = ListNode(-1)
        dummy_node.next = head 

        # 2. find the pre_left 
        count = 0
        pre_left = dummy_node
        while count < left - 1:
            pre_left = pre_left.next 
            count += 1 
        
        # 3. find the right 
        right_node = pre_left
        while count < right:
            right_node = right_node.next
            count += 1 
        
        post_right = right_node.next 

        # 4. seperate the left to right and reverse
        def reverse(start_node):
            prev = None 
            curr = start_node 

            while curr:
                next_node = curr.next
                curr.next = prev 
                prev = curr 
                curr = next_node
 
            return prev
        
        left_node = pre_left.next
        pre_left.next = None
        right_node.next = None

        reversed_list_head = reverse(left_node)
        pre_left.next = reversed_list_head 
        left_node.next = post_right
        return dummy_node.next 
      