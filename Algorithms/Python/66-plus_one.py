class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = []
        for digit in digits:
            num.append(str(digit))
        num = "".join(num)
        n = str(int(num) + 1)
        res = []
        for d in n:
            res.append(int(d))
        return res






        