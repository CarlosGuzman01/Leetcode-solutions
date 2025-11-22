class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0

        window = set()
        ans = 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            r += 1
            ans = max(ans, len(window))
            
        return ans


        