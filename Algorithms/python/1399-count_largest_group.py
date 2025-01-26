class Solution:
    def countLargestGroup(self, n: int) -> int:
        key = 1

        def dsum(n):
            res = [n]
            total = 0
            for x in str(n):
                total += int(x)
            res.append(total)
            return res
        
        map1 = {}

        for i in range(1, n + 1):
            og, sumd = dsum(i)

            if sumd not in map1:
                map1[sumd] = 1
            else:
                map1[sumd] += 1

            if map1[key] < map1[sumd]:
                key = sumd

        count = 0
        for h in map1:
            if map1[h] == map1[key]:
                count += 1

        return count






        