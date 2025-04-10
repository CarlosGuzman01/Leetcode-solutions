class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        md = float("inf")
        res = []
        j = 1

        while j < len(arr):
            cd = arr[j] - arr[j - 1]

            if md > cd:
                md = cd
                res = [[arr[j - 1], arr[j]]]

            elif md == cd:
                res.append([arr[j - 1], arr[j]])

            j += 1
        return res
