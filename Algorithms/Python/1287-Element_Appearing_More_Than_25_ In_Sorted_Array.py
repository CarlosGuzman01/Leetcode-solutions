class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        sus = 0.25 * len(arr)
        v = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if v == arr[i]:
                count += 1
                if count > sus:
                    return v
            else:
                v = arr[i]
                count = 1
           
        return arr[0]
            
        