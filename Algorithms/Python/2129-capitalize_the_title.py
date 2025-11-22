class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()

        for i in range(len(title)):
            title[i] = self.support(title[i])
        return " ".join(title)


    def support(self, s):
        if len(s) == 1 or len(s) == 2:
            return s.lower()
        
        return s.capitalize()
        