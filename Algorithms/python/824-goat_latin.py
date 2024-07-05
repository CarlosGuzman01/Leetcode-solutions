class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = []
        for i, s in enumerate(words):
            res.append(self.support(i, s))
        
        return " ".join(res)

    def support(self, i, s):
        x = s[0]
        if not self.isVowel(x.lower()):
            s = s[1:] + s[0]
        
        return s + "ma" + "a" * (i + 1)

    def isVowel(self, c):
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'