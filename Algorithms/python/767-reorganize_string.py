class Solution:
    def reorganizeString(self, s: str) -> str:
        myMap = Counter(s)
        heap = []

        for char, freq in myMap.items():
            heap.append([-freq, char])

        res = ""
        que = deque()
        heapq.heapify(heap)
        
        i = 0
        while heap:
            freq, char = heapq.heappop(heap)
            
            res += char
            
            freq = -freq -1
            
            if freq > 0:
                que.append([freq, char, i + 1])

            if que and que[0][2] == i:
                freq, char, time = que.popleft()
                heapq.heappush(heap, [-freq, char])
            i+=1

        if len(res) != len(s):
            return ""
        return res