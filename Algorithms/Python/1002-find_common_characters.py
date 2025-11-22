class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict1 = Counter(words[0])

        for i in range(1, len(words)):
            dict2 = Counter(words[i])

            for key in list(dict1.keys()):
                if key in dict2:
                    dict1[key] = min(dict1[key], dict2[key])
                else:
                    del dict1[key]
        
        list1 = []
        for key in dict1:
            for i in range(dict1[key]):
                list1.append(key)
            
        return list1


        

                    
