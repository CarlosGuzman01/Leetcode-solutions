class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        map1 = defaultdict(list)
        for i in range(len(s)):
            map1[s[i]].append(i)
        
        for key in map1:
            i = distance[ord(key) - ord('a')]

            if map1[key][1] - map1[key][0] -1 != i:
                return False

        
        return True
        