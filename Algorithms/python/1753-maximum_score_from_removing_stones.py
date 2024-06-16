class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        list1 = []

        list1.append(-a)
        list1.append(-b)
        list1.append(-c)

        heapq.heapify(list1)

        val1 = 1
        val2 = 1
        counter = 0
        while val1 > 0 and val2 > 0:
            val1 = abs(heapq.heappop(list1))
            val2 = abs(heapq.heappop(list1))

            counter += 1

            heapq.heappush(list1, -(val1 - 1))
            heapq.heappush(list1, -(val2 - 1))
        
        return counter - 1










        