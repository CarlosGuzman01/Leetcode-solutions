class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0].lower()
        counter = 0

        for i in range(1, len(s)):
            if prev != s[i].lower():
                counter += 1
            prev = s[i].lower()

        return counter
        



            