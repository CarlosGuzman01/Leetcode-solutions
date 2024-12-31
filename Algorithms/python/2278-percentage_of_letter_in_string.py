class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        myMap = Counter(s)
        return int(myMap[letter] / len(s) * 100)