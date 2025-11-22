class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res =  []
        myMap = {}
        arr2 =  sorted(set(arr))
            
        for i in range(len(arr2)):
            myMap[arr2[i]] = i + 1
        
        for n in arr:
            res.append(myMap[n])

        return res




        