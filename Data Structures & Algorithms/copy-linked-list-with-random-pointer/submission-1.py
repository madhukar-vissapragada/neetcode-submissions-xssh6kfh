"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy_node = Node(-1)
        temp_head = dummy_node
        temp = head 

        hash_map_a = {}
        hash_map_a[None] = None

        while temp:
            new_node = Node(temp.val)
            hash_map_a[temp] = new_node 
            dummy_node.next = new_node
            temp = temp.next
            dummy_node = dummy_node.next 
        
        temp = head 
        dummy_node = temp_head.next
        while temp:
            random_ptr_a = temp.random 
            random_ptr_b = hash_map_a[random_ptr_a]
            dummy_node.random = random_ptr_b 

            temp = temp.next 
            dummy_node = dummy_node.next 
        
        return temp_head.next 



        



        