# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.solve(root, result)

        return result 
    

    def solve(self, root, result):
        if root:
            result.append(root.val)
            self.solve(root.left, result)
            self.solve(root.right, result)