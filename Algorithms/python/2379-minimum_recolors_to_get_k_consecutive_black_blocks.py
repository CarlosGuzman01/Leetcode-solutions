class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        r = 0
        ans = k
        b = 0
        
        while r < len(blocks):

            if blocks[r] == "B":
                b += 1
            if r - l + 1 == k:
                ans = min(ans, k - b)
                if blocks[l] == "B":
                    b -= 1
                l += 1
            r += 1

        return ans
