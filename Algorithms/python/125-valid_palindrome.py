class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low <= high:
            while low < high and not self.alpha(s[low]):
                low += 1
            while low < high and not self.alpha(s[high]):
                high -= 1
            
            if s[low].lower() != s[high].lower():
                return False
                
            low += 1
            high -= 1
        return True
    
    def alpha(self, c):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

        