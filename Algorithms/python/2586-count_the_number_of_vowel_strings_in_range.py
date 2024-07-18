class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        

        for i in range(left, right + 1):
            if self.support(words[i][0]) and self.support(words[i][len(words[i]) -1]):
                count += 1
        return count
                

    def support(self, c):
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'