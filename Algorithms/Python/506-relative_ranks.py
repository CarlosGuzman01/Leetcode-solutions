class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [-x for x in score]
        heapq.heapify(heap)

        map1 = {}

        for i in range(len(score)):
            map1[abs(heapq.heappop(heap))] = i + 1

        res = []

        for n in score:
            temp = map1[n]
            if temp <= 3:

                if temp == 1:
                    res.append("Gold Medal")
                elif temp == 2:
                    res.append("Silver Medal")
                else:
                    res.append("Bronze Medal")
            else:
                res.append(str(temp))
        return res
