class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        l = len(n)
        counter = 0
        
        for i in range(l):
            if i + k > l:
                break
            temp = int(n[i: i + k])
            if temp != 0 and num % temp == 0:
                counter += 1
            i += 1
        return counter
            
            