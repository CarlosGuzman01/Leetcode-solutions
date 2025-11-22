# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []

        dummy = head
        ans = head

        while head:
            heap.append(head.val)
            head = head.next
        
        heapq.heapify(heap)
        
        while heap:
            dummy.val = heapq.heappop(heap)
            dummy = dummy.next

        return ans

        