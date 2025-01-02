class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        for i in range(len(word)):
            print(i)
            total += (i // 8) + 1

        return total
