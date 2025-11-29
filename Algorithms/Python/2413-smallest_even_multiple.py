class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        start = 2
        while not (start % n == 0 and start % 2 == 0):
            start += 1
        return start
        