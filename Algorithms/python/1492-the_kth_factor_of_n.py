class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        arr = []
        k -= 1
        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)
            
        if len(arr) - 1 < k:
            return -1
        return arr[k]
        