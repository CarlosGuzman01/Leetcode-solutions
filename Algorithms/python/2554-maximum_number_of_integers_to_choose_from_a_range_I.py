class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        total = 0

        s = set(banned)
        for x in range(1, n + 1):
            if total + x > maxSum:
                return count
            if x in s:
                continue
            count += 1
            total += x
            

        return count


        