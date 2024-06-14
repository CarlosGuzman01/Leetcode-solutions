class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dict1 = {}
        dict2 = {}

        p = s.split()

        if len(pattern) != len(p):
            return False

        for char, word in zip(pattern, p):

            if char in dict1 and dict1[char] != word:
                return False
            if word in dict2 and dict2[word] != char:
                return False

            dict1[char] = word
            dict2[word] = char

        return True
