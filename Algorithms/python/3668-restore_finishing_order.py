class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s = set()
        res = []
        for friend in friends:
            s.add(friend)
        for n in order:
            if n in s:
                res.append(n)
            if len(res) == len(friends):
                break
        return res

        