class Solution:
    def countEven(self, num: int) -> int:

        def func(x):
            res = 0
            for c in str(x):
                res += int(c)
            if res % 2 == 0:
                return True
            return False
        count = 0
        for i in range(num + 1):
            if func(i):
                count += 1
        return count - 1

        