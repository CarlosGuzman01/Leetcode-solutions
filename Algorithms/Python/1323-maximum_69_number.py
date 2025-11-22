class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        b = True
        for c in str(num):
            if c == '6' and b:
                res += '9'
                b = False
            else:
                res += c


        return int(res)
        