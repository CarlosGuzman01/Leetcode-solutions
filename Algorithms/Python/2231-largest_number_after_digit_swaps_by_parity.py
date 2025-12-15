class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []

        for n in str(num):
            n = int(n)
            if n % 2 == 0:
                even.append(-n)
            else:
                odd.append(-n)
        
        heapq.heapify(odd)
        heapq.heapify(even)

        res = []

        for n in str(num):
            if int(n) % 2 == 0:
                res.append(str(-heapq.heappop(even)))
            else:
                res.append(str(-heapq.heappop(odd)))
        st = "".join(res)
        return int(st)

        