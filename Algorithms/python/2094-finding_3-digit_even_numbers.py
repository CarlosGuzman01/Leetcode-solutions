class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        map1 = Counter(digits)

        def check(n):
            if n % 2 != 0:
                return False

            map2 = defaultdict(int)
            for c in str(n):
                c = int(c)
                map2[c] += 1
                if not c in map1:
                    return False
                elif map2[c] > map1[c]:
                    return False
            return True
        
        res = []
        for n in range(100, 999):
            if check(n):
                res.append(n)

        res.sort()
        return res


            

        