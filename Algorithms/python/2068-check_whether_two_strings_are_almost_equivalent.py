class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        map1 = Counter(word1)
        map2 = Counter(word2)

        for c in set(list(map1.keys()) + list(map2.keys())):
            if abs(map1[c] - map2[c]) > 3:
                return False
        return True
