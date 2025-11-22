# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que = deque([cloned])
        
        while que:
            node = que.popleft()

            if node.val == target.val:
                return node
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        
        