class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result = []
        i = 0
        while i + 1 < len(mountain):
            if i == 0:
                i += 1
                continue
            if i == len(mountain) - 1:
                i += 1
                continue
            
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                result.append(i)
            
            i += 1
        return result
            
