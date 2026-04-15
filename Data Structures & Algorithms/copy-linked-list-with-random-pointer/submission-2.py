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
        temp = head
        new_list = Node(-1)
        other = new_list
        hash_map = {}
        hash_map[None] = None

        while temp:
            new_node = Node(temp.val)
            hash_map[temp] = new_node 
            other.next = new_node 
            other = other.next 
            temp = temp.next
        
        temp = head 
        other = new_list.next 

        while temp:
            random_location = hash_map[temp.random] 
            other.random = random_location 

            temp = temp.next 
            other = other.next 
        
        return new_list.next 

            


    

        