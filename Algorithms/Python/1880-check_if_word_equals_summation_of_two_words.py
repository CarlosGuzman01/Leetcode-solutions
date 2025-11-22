class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def calc(s):
            total = 0
            for c in s:
                total *= 10
                digitVal = ord(c) - ord('a')
                total += digitVal
            return total
            
        return calc(firstWord) + calc(secondWord) == calc(targetWord)