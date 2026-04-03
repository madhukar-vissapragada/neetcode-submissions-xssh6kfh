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
        dummy = dummy_node
        temp = head 

        hash_map = {}
        hash_map[None] = None
        
        while temp:
            new_node = Node(temp.val)
            hash_map[temp] = new_node
            dummy.next = new_node 
            dummy = new_node 
            temp = temp.next
        
        temp_a = head
        temp_b = dummy_node.next 

        while temp_a:
            random_node_a = temp_a.random
            random_node_b = hash_map[random_node_a]
            temp_b.random = random_node_b 

            temp_a = temp_a.next 
            temp_b = temp_b.next 
        
        return dummy_node.next 

        
            

             
        
        
        

        