class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0
        count2 = 0

        half = len(s)//2

        for i in range(len(s)):

            if i >= half:
                if self.isVowel(s[i]):
                    count2 += 1
            else:
                if self.isVowel(s[i]):
                    count1 += 1

        return count1 == count2
    
    def isVowel(self , c):
        
        c = c.lower()
        mySet = {'a', 'e', 'i', 'o', 'u'}

        return c in mySet


        