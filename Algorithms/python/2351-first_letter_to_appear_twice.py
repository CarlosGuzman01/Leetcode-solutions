class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mySet = set()

        for c in s:
            if c in mySet:
                return c
            
            mySet.add(c)


        

        