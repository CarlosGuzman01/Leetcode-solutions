# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        que = deque([root])

        res = []

        while que:
            size = len(que)
            candidate = -9999999999
            for i in range(size):
                node = que.popleft()
                if node:
                    candidate = max(node.val, candidate)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)

            res.append(candidate)
        
        return res

        