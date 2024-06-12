class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        mySet = set(dictionary)
        
        boo = True
        result = ""
        for word in sentence.split():
            temp = ""
            for c in word:
                temp += c
                if temp in mySet:
                    result = result + temp + " "
                    boo = False
                    break
            if boo:
                result = result + word + " "
            boo = True
        
        return result.rstrip()



