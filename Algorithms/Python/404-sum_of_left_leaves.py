# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        leftsum = 0

        if root.left and not root.left.left and not root.left.right:
            leftsum += root.left.val

        leftsum += self.sumOfLeftLeaves(root.left)
        leftsum += self.sumOfLeftLeaves(root.right)

        return leftsum

         
        