# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.solve(root, 0, result)
        return result 
    

    def solve(self, root, level, result):
        if root:
            if len(result) == level:
                result.append([])
            
            result[level].append(root.val)
            self.solve(root.left, level + 1, result)
            self.solve(root.right, level + 1, result)
        

        