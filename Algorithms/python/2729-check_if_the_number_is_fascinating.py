class Solution:
    def isFascinating(self, n: int) -> bool:
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        t2 = n * 2
        t3 = n * 3
        st = str(n) + str(t2) + str(t3)
        for c in st:
            if c not in s or c == '0':
                return False
            s.remove(c)

        return len(s) == 0
        