class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        total = {}

        for arr in responses:
            s = set()
            for v in arr:
                if v not in s:
                    if v not in total:
                        total[v] = 0

                    total[v] += 1
                    s.add(v)

        max_freq = max(total.values())
        candidates = []
        for v, f in total.items():
            if f == max_freq:
                candidates.append(v)
        return min(candidates)
