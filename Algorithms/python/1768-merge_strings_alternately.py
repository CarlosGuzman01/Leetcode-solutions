class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        index = 0
        res = []
        while len(word1) - 1 >= index and len(word2) - 1 >= index:
            res.append(word1[index])
            res.append(word2[index])

            index += 1

        if len(word1) == len(word2):
            return "".join(res)
        
        if len(word1) > len(word2):

            while len(word1) - 1 >= index:
                res.append(word1[index])
                index += 1
        else:
            while len(word2) - 1 >= index:
                res.append(word2[index])
                index += 1
        return "".join(res)


        
             


