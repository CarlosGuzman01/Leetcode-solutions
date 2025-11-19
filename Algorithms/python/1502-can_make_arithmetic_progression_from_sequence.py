class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        j = i + 1
        prev = None        
        while j < len(arr):
            if prev == None:
                prev = arr[i] - arr[j]
            elif prev != arr[i] - arr[j]:
                return False
            
            i += 1
            j += 1
        
        return True
            
        