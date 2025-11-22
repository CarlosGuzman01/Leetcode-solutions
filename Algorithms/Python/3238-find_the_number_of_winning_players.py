class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        myMap = {}

        for arr in pick:
            x, y = arr

            if x in myMap and y in myMap[x]:
                myMap[x][y] += 1
            elif x in myMap and y not in myMap[x]:
                myMap[x][y] = 1
            
            else:
                myMap[x] = {y : 1}
        
        count = 0
        for n in myMap:
            if n == 0:
                count += 1
            else:
                for x in myMap[n]:
                    if myMap[n][x] > n:
                        count += 1
                        break            
        return count