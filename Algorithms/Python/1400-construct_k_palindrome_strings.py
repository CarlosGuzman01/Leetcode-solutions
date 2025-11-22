class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False

        myMap = Counter(s)
        oddCount = 0

        for key in myMap:
            if myMap[key] % 2 != 0:
                oddCount += 1

        return oddCount <= k




        


        