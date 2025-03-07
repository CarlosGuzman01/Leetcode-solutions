class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = False
        v = 0

        if len(arr) < 3:
            return False

        for i in range(len(arr)):
            if i != 0 and arr[i] > arr[i - 1]:

                v += 1
            if i != 0 and arr[i] <= arr[i - 1]:
                inc = True

            if inc and arr[i] >= arr[i - 1]:
                return False
        if v + 1 == len(arr) or v == 0:
            return False

        return True
