# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        que = deque([root])
        res = []

        while que:
            size = len(que)
            level = []
            for i in range(size):
                node = que.popleft()
                
                level.append(node.val)
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)

            if len(res) % 2 == 0:
                level.reverse()

            res.append(level)
        return res
