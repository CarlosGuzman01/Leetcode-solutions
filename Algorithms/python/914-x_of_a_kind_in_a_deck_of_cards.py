class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        myMap = Counter(deck)

        result = reduce(gcd, myMap.values())

        if result > 1:
            return True
        return False
        
       
        