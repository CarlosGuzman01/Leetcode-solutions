class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        arr = []

        for c in s:
            if c == '1':
                count += 1
            arr.append('0')

        if s[len(s) - 1] != 1:
            arr[len(arr) - 1] = '1'
            count -= 1
        i = 0
        while count > 0:
            if arr[i] != '1':
                arr[i] = '1'
                count -= 1
            i += 1

        
        return "".join(arr)
        