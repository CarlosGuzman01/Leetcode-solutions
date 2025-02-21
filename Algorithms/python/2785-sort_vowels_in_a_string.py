class Solution:
    def sortVowels(self, s: str) -> str:

        def is_vowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

        res = []
        heap = []

        for  c in s:
            if is_vowel(c.lower()):
                heap.append(c)
                res.append('$')
            else:
                res.append(c)

        heapq.heapify(heap)

        i = 0
        while heap:

            if res[i] == '$':
                res[i] = heapq.heappop(heap)
            i += 1
        

        return "".join(res)
        
