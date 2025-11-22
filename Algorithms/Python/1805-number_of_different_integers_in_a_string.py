class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        mySet = set()
        s = ""

        for c in word:
            if c.isdigit():
                s += c
            elif s != '':
                p = int(s)
                mySet.add(p)
                s = ""
        if s != '':
            mySet.add(int(s))
            
        return len(mySet)

        


        