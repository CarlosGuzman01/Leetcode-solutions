class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        counted = Counter(word)
        present = defaultdict(int)
        valid = set()
        res = 0

        for c in word:
            if c.islower() and c.upper() in present:
                continue
            elif c.isupper() and c.lower() in present and present[c.lower()] == counted[c.lower()] and c not in valid:
                valid.add(c)
                res += 1

            present[c] += 1
            

    
       
        return res





        
        