# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        self.traversal(root, 0, output)
        return output 
    

    def traversal(self, root: Optional[TreeNode], level: int, output: List[int]) -> None:
        if root:
            if len(output) == level:
                output.append([])
            
            output[level].append(root.val)
            
            self.traversal(root.left, level + 1, output)
            self.traversal(root.right, level + 1, output)
    
        