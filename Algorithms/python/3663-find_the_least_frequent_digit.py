class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        arr = [0] * 10
        for c in str(n):
            arr[int(c)]+=1
        
        ind = 999
        count = 999
        for i in range(len(arr)):
            if arr[i] == 0: continue
            if arr[i] < count:
                ind = i
                count = arr[i]
        return ind
        