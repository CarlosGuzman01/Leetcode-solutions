# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que = deque([root])

        res  = []

        while que:
            size = len(que)
            temp = 0

            for i in range(size):
                node = que.popleft()
                temp += node.val
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
            res.append(temp/size)
        return res

        