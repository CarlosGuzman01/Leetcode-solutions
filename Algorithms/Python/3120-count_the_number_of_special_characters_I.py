class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        mySet = set(word)
        counter = 0
        for c in mySet:
            if c.isupper():
                continue
            if c.upper() in mySet:
                counter += 1
        return counter
