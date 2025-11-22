class Solution:
    def frequencySort(self, s: str) -> str:
        map1 = Counter(s)
        map2 = defaultdict(list)

        for c in map1:
            map2[map1[c]].append(c)

        res = []

        for i in range(len(s), 0, -1):
            print(i)
            for c in map2[i]:
                res.append(c * i)

        return "".join(res)
