class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]

        for i in range(len(mat)):
            count = 0
            for n in mat[i]:
                if n == 1:
                    count += 1
            
            if res[1] < count:
                res[0] = i
                res[1] = count
        return res



        