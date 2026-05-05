# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.solve(root, result)

        return result 
    

    def solve(self, root, result):
        if root:
            self.solve(root.left, result)
            result.append(root.val)
            self.solve(root.right, result)
        
        