class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 0

        window = Counter()

        ans = 0

        while r < len(s):
            window[s[r]] += 1
            r += 1

            if r - l == 3:
                if len(window) == 3:
                    ans += 1
                window[s[l]] -= 1
                if window[s[l]] <= 0:
                    del window[s[l]]
                l += 1
        return ans





        