class Solution:
    def checkString(self, s: str) -> bool:
        b = False

        for c in s:
            if c == 'b':
                b = True
            if b and c == 'a':
                return False
        return True
        