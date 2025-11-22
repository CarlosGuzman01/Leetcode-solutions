class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        map1 = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            map1[groupSizes[i]].append(i)

            if len(map1[groupSizes[i]]) == groupSizes[i]:

                res.append(map1[groupSizes[i]])
                del map1[groupSizes[i]]
        return res
