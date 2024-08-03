class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        map1 = defaultdict(int)

        for x, y in zip(target, arr):
            map1[x] += 1
            map1[y] -= 1

        for n in map1:
            if map1[n] != 0:
                return False

        return True