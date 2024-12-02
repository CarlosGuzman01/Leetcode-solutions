class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        def support(w):
            for i in range(len(searchWord)):
                if i > len(w) - 1 or w[i] != searchWord[i]:
                    return False
            
            return True

        for i, w in enumerate(sentence.split()):
            if support(w):
                return i + 1
        return -1
        