class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        v1 = abs(x - z)
        v2 = abs(y - z)

        if v1 == v2:
            return 0
        elif v1 < v2:
            return 1
        return 2
        