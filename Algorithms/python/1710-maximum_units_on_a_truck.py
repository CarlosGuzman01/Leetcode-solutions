class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []

        heapq.heapify(heap)

        for arr in boxTypes:
            heapq.heappush(heap, [-arr[1], arr[0]])

        res = 0
        while heap and truckSize:
            units, boxes = heapq.heappop(heap)

            if boxes <= truckSize:
                res += units * boxes

                truckSize -= boxes
            else:
                res += units * truckSize

                truckSize = 0
        return -res


        

        