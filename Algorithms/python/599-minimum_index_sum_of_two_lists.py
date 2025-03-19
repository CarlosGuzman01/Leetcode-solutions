class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:


        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for i, n in enumerate(list1):
            m1[n] = i
        
        for i, n in enumerate(list2):
            m2[n] = i
        
        for key in list(m1.keys()):
            if key in m2:
                m1[key] = m1[key] + m2[key]
            elif key not in m2:
                del m1[key]
        
        val = 9999
        res = []

        for key in m1:
            if m1[key] < val:
                val = m1[key]
                res = [key]
            elif m1[key] == val:
                res.append(key)
        return res



        

            
        

        
        