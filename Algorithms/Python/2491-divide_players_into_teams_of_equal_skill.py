class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        x = skill[0]
        y = skill[len(skill) - 1]
        total = x + y
        
        low = 1
        high = len(skill) - 2
        chem = (x*y)
        while low < high:

            if skill[low] + skill[high] != total:
                return -1

            chem += (skill[low] * skill[high])

            low += 1
            high -=1
        

        return chem



        