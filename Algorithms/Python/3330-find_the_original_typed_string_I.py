class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        p = 0

        while p + 1 < len(word):
            if word[p] == word[p + 1]:
                count += 1
            p += 1
        return count + 1
        