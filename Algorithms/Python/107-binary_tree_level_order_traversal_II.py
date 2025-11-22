# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        que = deque([root])
        res = deque()
        while que:
            temp = []
            size = len(que)

            for i in range(size):
                node = que.popleft()
                temp.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.appendleft(temp)
        return list(res)
            


        