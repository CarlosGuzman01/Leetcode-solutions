# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        que = deque([root])

        while que:
            size = len(que)
            total = 0
            for _ in range(size):
                node = que.popleft()
                total += node.val
                if node.right: que.append(node.right)
                if node.left: que.append(node.left)
            
            heapq.heappush(heap, total)
            if len(heap) > k: heapq.heappop(heap)
        
        return -1 if len(heap) < k else heap[0]