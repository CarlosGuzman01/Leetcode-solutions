class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        que = deque()
        res = []

        for i in range(1, 10):
            que.append(i)

        while que:
            print(que)
            v = que.popleft()
            
            if v > high:
                return res
            if low <= v <= high:
                res.append(v)
            d = v % 10
            if d < 9:
                v = v * 10
                v += d + 1
                que.append(v)
        
        return res


        