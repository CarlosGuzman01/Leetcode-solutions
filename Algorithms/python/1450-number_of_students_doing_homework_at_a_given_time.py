class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        count = 0

        for x, y in zip(startTime, endTime):
            if x <= queryTime and y >= queryTime:
                count += 1

        return count 

        