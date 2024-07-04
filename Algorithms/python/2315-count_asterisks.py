class Solution:
    def countAsterisks(self, s: str) -> int:
        b = True
        counter = 0
        
        for c in s:
            if b and c == '*':
                counter += 1
            if c == '|':
                b = not b
            
        return counter
