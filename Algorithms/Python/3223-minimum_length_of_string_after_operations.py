class Solution:
    def minimumLength(self, s: str) -> int:

        myMap = Counter(s)
        count = 0
        for key in myMap:
            if myMap[key] & 1 == 0:
                count += 2
            else:
                count += 1
        return count


        