class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = []

        for c in s:
            st.append(str((ord(c) - ord('a')) + 1))
        
        st = "".join(st)
        while k:
            res = 0
            for c in st:
                res += int(c)
            st = str(res)

            k -= 1
        return res

        