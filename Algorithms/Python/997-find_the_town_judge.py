class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outcoming = defaultdict(int)

        for arr in trust:
            a, b = arr

            incoming[b] += 1
            outcoming[a] += 1
        
        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outcoming[i] == 0:
                return i
        return -1




       
        

       