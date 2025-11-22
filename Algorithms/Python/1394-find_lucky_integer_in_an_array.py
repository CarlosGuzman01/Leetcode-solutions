class Solution:
    def findLucky(self, arr: List[int]) -> int:

        lucky = -1
        map1 = Counter(arr)
        for key in map1:
            if map1[key] == key:
                lucky = max(lucky, key)
        return lucky
        