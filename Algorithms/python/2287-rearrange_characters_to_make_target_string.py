class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        map1 = Counter(target)
        map2 = Counter(s)
        
        res = 101
        for key in map1:
            res = min(map2[key]//map1[key], res)

        return res

        
        