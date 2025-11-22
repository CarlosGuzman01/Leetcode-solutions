class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myMap = Counter(arr)

        for n in arr:
            if n == 0 and myMap[n] == 1:
                continue
            if n * 2 in myMap:
                return True
        return False
        