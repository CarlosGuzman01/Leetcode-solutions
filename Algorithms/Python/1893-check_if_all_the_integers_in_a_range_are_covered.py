class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        s = set()

        for x in range(left, right + 1):
            s.add(x)

        for arr in ranges:
            for x in range(arr[0], arr[1] + 1):
                if x in s:
                    s.remove(x)
                if len(s) == 0:
                    return True

        return len(s) == 0
