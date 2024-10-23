# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                curSum += node.val
                return curSum == targetSum
            else:
                curSum += node.val

            return dfs(node.left, curSum) or dfs(node.right, curSum)
        

        return dfs(root, 0)
        