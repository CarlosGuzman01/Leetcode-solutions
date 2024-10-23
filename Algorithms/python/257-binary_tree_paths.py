# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        path = ""

        def dfs(node, ans, path):
            if node is None:
                return 
            elif node.left is None and node.right is None:
                path += str(node.val)
                ans.append(path)
            else:
                path += str(node.val) +"->" 
            
            dfs(node.left, ans, path) 
            dfs(node.right, ans, path) 

        dfs(root, ans, path)
       
        return ans
