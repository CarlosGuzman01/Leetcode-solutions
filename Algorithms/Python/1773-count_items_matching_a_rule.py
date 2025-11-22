class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0

        if ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        else:
            index = 0
        
        for things in items:
            if things[index] == ruleValue:
                res += 1

        return res
        