# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        l = 0

        que = deque([root])

        while que:
            size = len(que)
            level = deque()
            for i in range(size):
                node = que.popleft()
                if l % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if len(level) != 0 and level[-1] >= node.val:
                        return False

                if l % 2 != 0:
                    if node.val % 2 != 0:
                        return False
                    if len(level) != 0 and level[-1] <= node.val:
                        return False
                
                level.append(node.val)
                if len(level) > 1: level.popleft()
                
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                

            l+=1
        return True
                








        