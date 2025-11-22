class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        seen = set()
        common = 0
        res = []

        for i in range(len(A)):
            if A[i] in seen:
                common += 1
            seen.add(A[i])

            if B[i] in seen:
                common += 1
            seen.add(B[i])

            res.append(common)

        return res
